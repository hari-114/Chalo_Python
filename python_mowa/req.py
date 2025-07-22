import requests as rq
import re
r = rq.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text
text=re.findall(r'>([^<>]+)<',html)
line=[part.strip() for part in text if part.strip()]