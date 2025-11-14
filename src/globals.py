import json, utils

with open("config/Sitefile", 'r') as f:
    sitefile = json.loads(utils.rmcomments(f.read()))



with open("src/templates/template.html", 'r') as f:
    template = f.read()