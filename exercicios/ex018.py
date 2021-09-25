# Faça um programa que leia um ângulo qualquer e mostre na tela o seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Digite um ângulo em graus: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno de {0}° é {1:.2f}\nO cosseno de {0}° é {2:.2f}\nA tangente de {0}° é {3:.2f}'.format(ang,sen,cos,tan))