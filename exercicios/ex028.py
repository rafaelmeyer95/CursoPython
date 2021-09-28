"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu"""
from random import random
from time import sleep

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'bverde':'\033[1;32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'bazul':'\033[1;34m',
         'roxo':'\033[35m'}

num = int(random()*5)+1

print('{}Eu estou pensando em número {}inteiro{} de 1 a 5, será que você consegue adivinhar?{} '.format(cores['azul'],cores['bazul'],cores['azul'],cores['limpa']))
num2 = int(input(''))

print(('{}-{}-{}-{}-{}-{}'.format(cores['vermelho'],cores['amarelo'],cores['azul'],cores['roxo'],cores['verde'],cores['limpa']))*6)
print(' '*10+'{}C{}A{}R{}R{}E{}G{}A{}N{}D{}O{}'.format(cores['vermelho'],cores['amarelo'],cores['azul'],cores['roxo'],cores['verde'],cores['vermelho'],cores['amarelo'],cores['azul'],cores['roxo'],cores['verde'],cores['limpa']))
print(('{}-{}-{}-{}-{}-{}'.format(cores['vermelho'],cores['amarelo'],cores['azul'],cores['roxo'],cores['verde'],cores['limpa']))*6)

sleep(1)

for i in range (28):
    print('','{}#{}'.format(cores['bazul'],cores['limpa'])*i)
    sleep(.1)

print(('{}-{}-{}-{}-{}-{}'.format(cores['vermelho'],cores['amarelo'],cores['azul'],cores['roxo'],cores['verde'],cores['limpa']))*6)
if num == num2:
    print('   {}parabéns, você acertou!!!\n        o número era {}!{}'.upper().format(cores['bverde'],num,cores['limpa']))
else:
    print(' '*2 +'{}Você errou, o número era {}.{}'.upper().format(cores['vermelho'],num,cores['limpa']))

print(('{}-{}-{}-{}-{}-{}'.format(cores['vermelho'],cores['amarelo'],cores['azul'],cores['roxo'],cores['verde'],cores['limpa']))*6)



