import json
from urllib.request import urlopen

with urlopen('http://challenges.neverlanctf.com:1120') as r:
    print(r.read())
