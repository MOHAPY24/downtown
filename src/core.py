import markdown # pyright: ignore[reportMissingModuleSource]
from bs4 import BeautifulSoup
from globals import *
import sys
from pathlib import Path





def build():

    for i in sitefile["Files"]:
        print(f"[*] Making: '{sitefile["Files"][i]}'")
        soup = BeautifulSoup(template, "html.parser")
        body = soup.body
        with open(sitefile["Files"][i], 'r') as f:
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

        filen = Path(i).stem
        with open(f"build/out/{filen}.html", 'w') as f:
            f.write(soup.prettify())

try:
    mode = sys.argv[1]
except IndexError:
    print("[X] No mode given!")
    exit(1)

if mode == "build":
    build()