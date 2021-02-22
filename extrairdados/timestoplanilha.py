import requests
from bs4 import BeautifulSoup
import csv

cont = 0
i = 0
j = 0


source = requests.get('https://lol.gamepedia.com/CBLOL/2021_Season/Split_1').text

soup = BeautifulSoup(source, 'html.parser')

puxartimes = soup.find_all('th', "tournament-roster-header")
nomestimes = []

for n in puxartimes:
    nomestimes.append(n.text)

print(nomestimes)

with open('newFile.csv', 'a') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for word in nomestimes:
        wr.writerow([word])

"""with open('baronweek5.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(itembaron)
    writer.writerow(listatime)
    writer.writerow(partidas)"""
