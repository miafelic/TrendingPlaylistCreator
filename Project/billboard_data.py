import requests
from bs4 import BeautifulSoup
import json

def get_billboard_data():
    req = requests.get("https://www.billboard.com/charts/hot-100/")
    req.raise_for_status()

    billboard = BeautifulSoup(req.text, 'lxml')
    containers = billboard.find_all('div', class_='o-chart-results-list-row-container')


    exclude = ["NEW", "Facebook", "Twitter", "Embed", "Copy Link", "RE-ENTRY"]

    song_data = {}
    for i, container in enumerate(containers, start=1):
        song_title = container.find('h3').text.strip()
        look = 1
        search = container.select('span')
        artist = search[look].text.strip()
        while "".join(artist.split()) in exclude or artist.isnumeric():
            look += 1
            artist = search[look].text.strip()

        song_data[i] = {artist:song_title}


    with open("./Project/song_data.json", "w") as sd:
        json.dump(song_data, sd, indent=4)

    return song_data
