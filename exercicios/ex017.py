# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
from math import hypot

cato = float(input('Informe o comprimento do cateto oposto: '))
cata = float(input('Informe o comprimento do cateto adjacente: '))

print("O comprimento da hipotenusa é: {:.2f}.".format(math.hypot(cato,cata)))