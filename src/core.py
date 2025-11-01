import markdown, utils, json # pyright: ignore[reportMissingModuleSource]
from bs4 import BeautifulSoup

final_HTML = ""

with open("config/Sitefile", 'r') as f:
    sitefile = json.loads(utils.rmcomments(f.read()))


with open("src/configs/template.html", 'r') as f:
    template = f.read()

soup = BeautifulSoup(template, "html.parser")
body = soup.body


with open(sitefile["Files"]["Index"], 'r') as f:
    mark = f.read()

soup.title.string = sitefile["metadata"]["Title"]
meta_desc = soup.find("meta", attrs={"name": "description"})
stylesheet = soup.find("link", attrs={"rel": "stylesheet"})

if stylesheet:
    stylesheet["href"] = sitefile["metadata"]["Stylesheet-file"]
else:
    new_link = soup.new_tag("link", rel="stylesheet", href=sitefile["metadata"]["Stylesheet-file"])
    soup.head.append(new_link)

if meta_desc:
    meta_desc["content"] = sitefile["metadata"]["Description"]
else:
    new_meta = soup.new_tag("meta")
    new_meta.attrs["name"] = "description"
    new_meta.attrs["content"] = sitefile["metadata"]["Description"]
    soup.head.append(new_meta)

body.append(BeautifulSoup(markdown.markdown(mark), "html.parser"))

with open("build/out/index.html", 'w') as f:
    f.write(soup.prettify())