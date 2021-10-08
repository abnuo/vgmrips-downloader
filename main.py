import vgmrips
import os
import requests
from urllib.parse import urlparse, unquote

url = input("URL of pack to download:\n")
if not url.startswith("https://vgmrips.net/packs/pack/"):
  exit("URL is not a vgmrips pack url.")
pack = vgmrips.getPack(url)
dir = vgmrips.getPackTitle(url) + "/"
os.mkdir(dir)
for i in pack:
  print("Downloading " + i)
  r = requests.get(i)
  with open(dir + unquote(os.path.basename(urlparse(i).path)), "wb") as f:
    f.write(r.content)
print("Downloaded to directory \"" + dir[0:len(dir)-1] + "\"")
