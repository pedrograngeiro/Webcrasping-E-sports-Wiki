import requests
from bs4 import BeautifulSoup

cont = 0
i = 0
j = 0

source = requests.get('https://lol.gamepedia.com/CBLOL/2021_Season/Split_1/Scoreboards').text

soup = BeautifulSoup(source, 'html.parser')

barons = soup.find_all('div', "sb-footer-item sb-footer-item-barons")


dias = soup.find_all('span', "mw-headline")
times = soup.find_all('span', "teamname")

listatime = []
partidas = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
itembaron = []

for baron in barons:
    itembaron.append(int(baron.text))

for time in times:
    listatime.append(time.text)

for l in range(0,len(partidas)):
    for c in range(0,2):
        partidas[l][c] = listatime[i]
        i = i + 1
##################### VISUALIZAÇÃO BONITA #######################
print("-=" * 30)
for l in range(0,len(partidas)):
    print("==Partida==", (l+1))

    for c in range(0,2):
        print( partidas[l][c])

        print("Barons: ", end='') #Contagem de barons por time
        print(itembaron[cont])
        cont = cont + 1

    print()

#################### FIM VISULIZAÇÃO BONITA #####################
