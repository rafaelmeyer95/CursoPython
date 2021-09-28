# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#update

a = float(input('Digite o comprimento do primeiro vértice: '))
b = float(input('Digite o comprimento do segundo vértice: '))
c = float(input('Digite o comprimento do terceiro vértice: '))

if a + b < c or a + c < b or b + c < a:
    print('Os valores indicados não podem formar um triângulo')
else:
    print('Os valores indicados podem formar um triângulo')