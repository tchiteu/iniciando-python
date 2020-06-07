# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv = pd.read_csv('./util/the_game_awards.csv', converters={i: str for i in range(100)})

anos = csv['year'].unique()
jogos = csv.groupby(['nominee']).size().reset_index(name='count')
jogos = jogos.sort_values(by=['count'], ascending=False).head(10)
premios = []

# Desenhando o gráfico

fig, ax = plt.subplots()

def buscaPremios(jogo, ano):
  result = csv[csv.nominee == jogo]
  result = result.loc[result.year == ano, 'year'].count()
  return result


for jogo in jogos['nominee']:
  qtdPremio = 0
  for ano in anos:
    qtdPremio += buscaPremios(jogo, ano)
    premios.append(qtdPremio)
  ax.plot(anos, premios, label=jogo)
  premios = []

ax.set_xticklabels(anos)

ax.set(xlabel='Ano', ylabel='Quantidade de premios')
ax.set_title('Premiacoes de Jogos')
ax.legend()
ax.grid()

fig.savefig("grafico_aula4.png")
plt.show()