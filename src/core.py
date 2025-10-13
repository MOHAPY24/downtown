import markdown
from bs4 import BeautifulSoup
from globals import *
import sys
from pathlib import Path





def build():

    for i in sitefile["Files"]:
        savesite = sitefile
        if i != "Index":
            try:
                with open(f"build/configs/{i}.Site", 'r') as f:
                    savesite = json.loads(utils.rmcomments(f.read()))
            except FileNotFoundError:
                print(f"[*] WARNING: Using stock Sitefile configuration for '{sitefile["Files"][i]}', No '{i}.Site' file found...")
                pass
        print(f"[*] Building: '{sitefile["Files"][i]}'")
        soup = BeautifulSoup(template, "html.parser")
        body = soup.body
        try:
            with open(sitefile["Files"][i], 'r') as f:
                mark = f.read()
        except:
            print(f"[X] Err in Sitefile: File '{sitefile["Files"][i]}' does not exist or has an invalid path")
            exit(1)

        soup.title.string = savesite["metadata"]["Title"]
        meta_desc = soup.find("meta", attrs={"name": "description"})
        stylesheet = soup.find("link", attrs={"rel": "stylesheet"})

        if stylesheet:
            with open(f"build/out/{Path(savesite['metadata']['Stylesheet-file']).stem}.css", 'w') as f:
                try:
                    with open(savesite["metadata"]["Stylesheet-file"], 'r') as r:
                        f.write(r.read())
                except FileNotFoundError:
                    print(f"[X] Stylesheet: '{savesite["metadata"]["Stylesheet-file"]}' does not exist or is an invalid path.")
                    exit(i)
            stylesheet["href"] = savesite["metadata"]["Stylesheet-file"]
        else:
            new_link = soup.new_tag("link", rel="stylesheet", href=savesite["metadata"]["Stylesheet-file"])
            soup.head.append(new_link)

        if meta_desc:
            meta_desc["content"] = savesite["metadata"]["Description"]
        else:
            new_meta = soup.new_tag("meta")
            new_meta.attrs["name"] = "description"
            new_meta.attrs["content"] = savesite["metadata"]["Description"]
            soup.head.append(new_meta)
            with open(f"build/out/{Path(savesite['metadata']['Stylesheet-file']).stem}.css", 'w') as f:
                try:
                    with open(savesite["metadata"]["Stylesheet-file"], 'r') as r:
                        f.write(r.read())
                except FileNotFoundError:
                    print(f"[X] Stylesheet: '{savesite["metadata"]["Stylesheet-file"]}' does not exist or is an invalid path.")
                    exit(i)

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