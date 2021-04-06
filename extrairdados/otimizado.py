import requests
from bs4 import BeautifulSoup
import csv

# Inicializei as variáreis
i = 0
j = 0


source = requests.get('https://lol.fandom.com/wiki/CBLOL/2021_Season/Split_1_Playoffs/Scoreboards').text

soup = BeautifulSoup(source, 'html.parser')
pesquisadefinida = soup.find_all('div', "sb-header-Kills")

numpartidas = int(input("Digite o numero de partidas: "))
partidas = []

for i in range(0, numpartidas):
    partidas.append([0,0])

numdados = []

numDadosTime1Time2 = []

for i in range(0, numpartidas):
    numDadosTime1Time2.append([0,0])

for dados in pesquisadefinida:
    numdados.append(dados.text)

for linha in range(0,numpartidas):
    for coluna in range(0,2):
        numDadosTime1Time2[linha][coluna] = numdados[j]
        j = j + 1


print(numDadosTime1Time2)

with open('final.csv', 'a', newline="") as csvfile:

    wr = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
    for word in numDadosTime1Time2:
        wr.writerow(word)