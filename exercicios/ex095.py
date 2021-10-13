# Aprimore o exercício 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização
# de detalhes do aproveitamento de cada jogador.

dados = dict()
dados2 = list()
gols = list()
total = 0

while True:
    dados['Nome'] = str(input('Nome: ')).title()
    partidas = int(input(f'Quantas partidas {dados["Nome"].title()} jogou?  '))

    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
        total += gols[i]

    dados['Gols'] = gols[:]
    dados['Total'] = total
    dados2.append(dados.copy())
    gols.clear()
    total = 0

    continua = str(input('Quer continuar? [S/N] '))
    while continua not in 'SsnN':
        print('Entrada inválida, tenta novamente!')
        continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        break

print('-='*25)
print(' Cod          Nome            Gols          Total')
print('-'*50)
for p,jogador in enumerate(dados2):
    print(f'{p+1:^5}',end='    ')
    for key,value in jogador.items():
        print(f'{str(value):^15}',end='')
    print()
print('-'*50)
while True:
    num = int(input('Mostrar dados de qual jogador? (0 para parar) '))
    if num == 0:
        break
    while num < 0 or num > len(dados2):
        print('Entrada inválida, tente novamente!')
        num = int(input('Mostrar dados de qual jogador? (0 para parar)'))
    print(f'LEVANTAMENTO DO JOGADOR: {dados2[num-1]["Nome"]}')
    for p,g in enumerate(dados2[num-1]['Gols']):
        print(f'No jogo {p+1} fez {g} gols')


