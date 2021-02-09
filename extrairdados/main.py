import requests
from bs4 import BeautifulSoup

res = requests.get("https://lol.gamepedia.com/LPL/2021_Season/Spring_Season/Scoreboards")

res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

scoreboards = soup.find_all(class_="sb")

all_scoreboards = []

    info = scoreboards.find(class_="sb-teamname")
    info = info.get_text()
    print(info)