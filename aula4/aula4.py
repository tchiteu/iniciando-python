# coding: utf-8

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# csv = pd.read_csv('./util/the_game_awards.csv', converters={i: str for i in range(100)})
# csv = csv.groupby(['nominee']).size().reset_index(name='count')
# csv = csv.sort_values(by=['count'], ascending=False).head(10)

# Montando gráfico

# labels = []
# means = []

# width = 0.35
# x = np.arange(len(labels))
# fig, ax = plt.subplots()

# for i in range(10):
#   labels.append(csv[i:i + 1]['nominee'].iloc[0])
#   means.append(csv[i:i + 1]['count'].iloc[0])

#   react = ax.bar(i * 0.4, means[i], width, label=labels[i])


# ax.set_title("Jogos com mais premiacoes oficiais")
# ax.set_ylabel('Quantidade de premios')

# ax.set_xticks(x)
# ax.set_xticklabels(labels)

# ax.legend()

# fig.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv = pd.read_csv('./util/the_game_awards.csv', converters={i: str for i in range(100)})

anos = csv['year'].unique()
jogos = csv.groupby(['nominee']).size().reset_index(name='count')
jogos = jogos.sort_values(by=['count'], ascending=False).head(10)

# Desenhando o gráfico

fig, ax = plt.subplots()

def buscaPremios(jogo, ano):
  result = csv[csv.nominee == jogo]
  result = result.loc[result.year == ano, 'year'].count()
  return result

for ano in anos:
  for jogo in jogos['nominee']:
    qtdPremio = buscaPremios(jogo, ano)
    print(jogo, ano, qtdPremio)
  

s = [1, 2, 4, 0, 0, 0]
a = [2, 4, 1, 2, 0, 10]

ax.plot(anos, s)
ax.plot(anos, a)

ax.set_xticklabels(anos)

ax.set(xlabel='time (s)', ylabel='voltage (mV)')
ax.set_title('Premiacoes de Jogos')
ax.grid()

fig.savefig("grafico_aula4.png")
# plt.show()