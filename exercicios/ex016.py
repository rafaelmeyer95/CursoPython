# Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira

import math

num = float(input('Digite um número: '))

print('A porção inteira de {} é {}.'.format(num,math.trunc(num)))

