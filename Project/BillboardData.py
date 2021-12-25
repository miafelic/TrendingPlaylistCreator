import requests
from bs4 import BeautifulSoup
import json


req = requests.get("https://www.billboard.com/charts/hot-100/")
req.raise_for_status()

billboard = BeautifulSoup(req.text, 'lxml')
containers = billboard.find_all('div', class_='o-chart-results-list-row-container')
# print(containers[99].find('h3').text.strip())

exclude = ["NEW", "Facebook", "Twitter", "Embed", "Copy Link", "RE-ENTRY"]
a = containers[84].select('span')
# test = a[2].text.strip()
# # print(test)
# culprit = a[1].text.strip()
# print("".join(culprit.split()))

for i, container in enumerate(containers, start=1):
    look = 1
    song_title = container.find('h3').text.strip()
    search = container.select('span')
    artist = search[look].text.strip()
    while "".join(artist.split()) in exclude or artist.isnumeric():
        look += 1
        artist = search[look].text.strip()

    print(i, artist)

