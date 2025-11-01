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
body.append(BeautifulSoup(markdown.markdown(mark), "html.parser"))

with open("build/out/index.html", 'w') as f:
    f.write(soup.prettify())