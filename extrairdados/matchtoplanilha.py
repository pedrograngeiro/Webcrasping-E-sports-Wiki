import requests
from bs4 import BeautifulSoup
import csv

dia = int(input("Digite o dia 1 ou 2 etc: "))
numpartidas = int(input("Digite o numero de partidas do dia: "))
numpartidasold = numpartidas
numpartidas = numpartidas * dia

cont = 0
i = 0
j = 0


source = requests.get('https://lol.gamepedia.com/CBLOL/2021_Season/Split_1/Scoreboards').text

soup = BeautifulSoup(source, 'html.parser')
times = soup.find_all('span', "teamname")

listatime = []
partidas = []

for i in range(0,numpartidasold):
    partidas.append([0,0])

print(partidas)





print(listatime)

"""with open('newFile.csv', 'a') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for word in partidas:
        wr.writerow([None,[word]])
"""