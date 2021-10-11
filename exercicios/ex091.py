# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
from operator import itemgetter

dados = {'Player1': randint(1,6),
         'Player2': randint(1,6),
         'Player3': randint(1,6),
         'Player4': randint(1,6)}

for k, v in dados.items():
    print(f'O {k} tirou {v}.')
    sleep(1)


dados = sorted(dados.items(), key=itemgetter(1), reverse=True)  # Coloca em ordem decrescente dos valores

print(15*'-=')

for p, v in enumerate(dados):
    print(f'{p+1}º colocado: {v[0]} com {v[1]}')
    sleep(1)


