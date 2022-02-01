# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome='desconhecido',gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s).')

            # Programa Principal

jogador = input("Nome do Jogador: ")
ngols = input("Número de Gols: ")

if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if jogador.strip() == '':
    ficha(gols = ngols)
else:
    ficha(jogador,ngols)