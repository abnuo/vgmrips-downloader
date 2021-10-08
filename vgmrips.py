import requests
import random
from bs4 import BeautifulSoup

def getrandomVGM():
    r = requests.get('https://vgmrips.net/packs/random')
    urls = []
    soup = BeautifulSoup(r.text)
    songs = soup.find("div", {"id": "details"})
    table = soup.find("table", {"class": "playlist"})
    tbody = soup.find("tbody")
    for item in tbody.find_all('tr'):
        if 'data-audiourl' in str(item):
            urls.append(item['data-audiourl'])
    url = random.choice(urls)
    print("Downloading " + url)
    r2 = requests.get(url)
    with open('music.mp3', 'wb') as f:
        f.write(r2.content)
    return url

def getPack(pack_url="https://vgmrips.net/packs/pack/dragon-saber-after-story-of-dragon-spirit-namco-system-2"):
    r = requests.get(pack_url)
    urls = []
    soup = BeautifulSoup(r.text)
    songs = soup.find("div", {"id": "details"})
    table = soup.find("table", {"class": "playlist"})
    tbody = soup.find("tbody")
    for item in tbody.find_all('tr'):
        if 'data-audiourl' in str(item):
            urls.append(item['data-audiourl'])
    return urls
