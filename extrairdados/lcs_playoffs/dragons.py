import requests
from bs4 import BeautifulSoup
import csv

cont = 0
i = 0
j = 0


source = requests.get('https://lol.gamepedia.com/LCS/2021_Season/Mid-Season_Showdown/Scoreboards').text

soup = BeautifulSoup(source, 'html.parser')
times = soup.find_all('span', "teamname")
kills = soup.find_all('div', "sb-footer-item sb-footer-item-dragons")

numpartidas = 4
listatime = []
partidas = [[0,0],[0,0],[0,0],[0,0]]
numkills = []
numdragonspartidas = [0,0],[0,0],[0,0],[0,0]


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
        numdragonspartidas[linha][coluna] = numkills[j]
        j = j + 1


print(numdragonspartidas)
"""with open('newFile.csv', 'a') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for word in partidas:
        wr.writerow([None,[word]])
"""

with open('lcsplayoffs_quartas_dragons', 'a', newline="") as csvfile:

    wr = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
    for word in partidas:
        wr.writerow(word)
    for word in numdragonspartidas:
        wr.writerow(word)