import requests
from bs4 import BeautifulSoup

cont = 0
i = 0
j = 0

source = requests.get('https://lol.gamepedia.com/CBLOL/2021_Season/Split_1/Scoreboards/Week_4').text

soup = BeautifulSoup(source, 'lxml')


dias = soup.find_all('span', "mw-headline")
times = soup.find_all('span', "teamname")
#vs = soup.find_all('th', "sb-teamname-vs")

listatime = []
partidas = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for time in times:
    listatime.append(time.text)

for l in range(0,len(partidas)):
    for c in range(0,2):
        partidas[l][c] = listatime[i]
        i = i + 1

print("-=" * 30)
for l in range(0,len(partidas)):
    for c in range(0,2):
        print( partidas[l][c])
    print()