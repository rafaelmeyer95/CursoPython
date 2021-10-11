# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato

dados = dict()
gols = list()
total = 0

dados['Nome'] = str(input('Nome: ')).title()
partidas = int(input(f'Quantas partidas {dados["Nome"].title()} jogou?  '))

for i in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    total += gols[i]

dados['Gols'] = gols
dados['Total'] = total

print(20*'-=')
print(dados)
print(20*'-=')
for k,v in dados.items():
    print(f'{k}: {v}')
print(20*'-=')
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for i in range(partidas):
    print(f'Na partida {i+1}, fez {dados["Gols"][i]} gols.')
print(f'Total de gols: {total}')