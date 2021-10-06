# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
# de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100))

print(f'Os números sorteados foram: {numeros}')
print(f'O menor valor entre os sorteados é {min(numeros)}\nO maior valor entre os sorteados é {max(numeros)}')
