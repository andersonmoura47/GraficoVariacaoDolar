# coding: utf-8
# fonte: https://www.cepea.esalq.usp.br/br/serie-de-preco/dolar.aspx?todos=true
# os valores foram multiplicados por 10.000 pois estavam com (,) e não ponto (.)
# portanto o python não aceita como inteiro

import matplotlib.pyplot as plt

dados = open('csv_dolar2.csv').readlines()  # le os dados
# print(dados)

anos = []
vr = []

for i in range(len(dados)):
    if i != 0:    # salta a primeira linha (Cabeçalho)
        linhas = dados[i].split(';')  # split separa os dados
        valor = int(linhas[2]) / 10000  # coleta os valores *10k e transforma no valor correto ex: R$4.3192
        vr.append(valor)
        anos.append(i)

plt.title('Variações do Dólar 1996-2020')
plt.xlabel("<== Tempo")
plt.ylabel('RS/USD')
plt.plot(anos, vr, color='green')
# plt.savefig("Graficos Python - Dolar.pdf")
plt.show()
