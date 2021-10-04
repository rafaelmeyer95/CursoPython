# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vit = 0

while True:
    jogador = int(input('Digite um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] '))
    maquina = randint(1,10)
    print(f'Você escolheu {jogador} e o computador escolheu {maquina}')
    if pi in 'Pp' and (jogador+maquina)%2 == 0 or pi in 'Ii' and (jogador+maquina)%2 == 1:
        vit += 1
    else:
        break
print(f'Jogo encerrado!\nTotal de vitórias: {vit}.')