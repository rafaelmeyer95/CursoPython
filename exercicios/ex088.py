from random import randint
from time import sleep

jogos = []
jogo = []

print('-'*30)
print('          MEGA SENA          ')
print('-'*30)

n = int(input('Quantos jogos você quer? '))

for i in range(n):
    for j in range(6):
        num = randint(1,60)
        while num in jogo:
            num = randint(1,60)
        jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

print('-'*30)
print('       SORTEANDO JOGOS      ')
print('-'*30)

for i in range(n):
    sleep(1)
    print(f'Jogo {i+1}: {jogos[i]}')
