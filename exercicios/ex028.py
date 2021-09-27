"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu"""
from random import random

num = int(random()*5)+1

num2 = int(input('Adivinhe o número inteiro de 1 a 5: '))
print('-'*30)

if num == num2:
    print('Você acertou, o número era {}!'.format(num))
else:
    print('Você errou, o número era {}.'.format(num))

print('-'*30)



