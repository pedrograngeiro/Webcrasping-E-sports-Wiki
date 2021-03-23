import requests
from bs4 import BeautifulSoup
import csv

cont = 0
i = 0
j = 0


source = requests.get('https://lol.gamepedia.com/LPL/2021_Season/Spring_Season/Scoreboards/Week_6_(3)').text

soup = BeautifulSoup(source, 'html.parser')
times = soup.find_all('span', "teamname")
kills = soup.find_all('div', "sb-header-Kills")

numpartidas = 14
listatime = []
partidas = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
numkills = []
numpartidaskills = [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]


print(partidas)

for time in times:
    listatime.append(time.text)

for l in range(0,numpartidas):
    for c in range(0,2):
        partidas[l][c] = listatime[i]
        i = i + 1


for kill in kills:
    numkills.append(kill.text)

for linha in range(0,numpartidas):
    for coluna in range(0,2):
        numpartidaskills[linha][coluna] = numkills[j]
        j = j + 1


print(numpartidaskills)
"""with open('newFile.csv', 'a') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for word in partidas:
        wr.writerow([None,[word]])
"""

with open('newFile copia.csv', 'a', newline="") as csvfile:

    wr = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
    for word in partidas:
        wr.writerow(word)
    for word in numpartidaskills:
        wr.writerow(word)