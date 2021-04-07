import requests
from bs4 import BeautifulSoup
import csv

# Inicializei as variáreis
i = 0
j = 0

# inicializei listas vazias
partidas = []
numdados = []
numDadosTime1Time2 = []


source = requests.get('https://lol.fandom.com/wiki/CBLOL/2021_Season/Split_1_Playoffs/Scoreboards').text #chama código fonte do link e armazena na variavél

soup = BeautifulSoup(source, 'html.parser') #separa o html
pesquisadefinida = soup.find_all('div', "sb-header-Kills") #pesquisa os atributos que você quer

numpartidas = int(input("Digite o numero de partidas: ")) #armazena o número de jogos do dia

for i in range(0, numpartidas): #loop para add os elementos [0,0] dentro da lista até o numero de partidas definidas
    partidas.append([0,0])

for i in range(0, numpartidas): #loop para add os elementos [0,0] do time 1 e time 2 dentro da variável "numDadosTime1Time2"
    numDadosTime1Time2.append([0,0])

#variavel "dados" é por padrão inicializada em 0
for dados in pesquisadefinida: # loop percorrendo de 0 até o fim de "pesquisadefinida"
    numdados.append(dados.text) # add dentro da lista "numdados" o conteudo puxado em "pesquisadefinida" formatado em texto


#Optei por utilizar o método de matriz(tabelas) para armazenar os dados
for linha in range(0,numpartidas): # loop de linha percorrendo de 0 até o número de partidas
    for coluna in range(0,2): # loop definindo que teremos somente 2 colunas
        numDadosTime1Time2[linha][coluna] = numdados[j] #numdados acompanhando linha e coluna conforme. E armazenando o conteudo em cada.
        j = j + 1


print(numDadosTime1Time2)

with open('final.csv', 'a', newline="") as csvfile: #Escreve no arquivo csv já criado

    wr = csv.writer(csvfile,quoting=csv.QUOTE_ALL)
    for word in numDadosTime1Time2:
        wr.writerow(word)