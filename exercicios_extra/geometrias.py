# Escreva um programa que calcule o perímetro e a área de algumas geometrias: retângulo, triângulo retângulo e círculo.

from math import sqrt,pi

while True:
    figura = int(input('Qual o tipo da geometria?\n(1) Retângulo\n(2) Triângulo\n(3) Círculo\n'))
    x = int(input('O que você deseja calcular?\n(1) Área\n(2) Perímetro\n(3) Área e Perímetro\n'))

    if figura == 1:
        base = float(input('Digite o comprimento da base do retângulo: '))
        altura = float(input('Digite o comprimento da altura do retângulo: '))
        area = base*altura
        perimetro = 2*(base+altura)

    elif figura == 2:
        base = float(input('Digite o comprimento da base do triângulo retângulo: '))
        altura = float(input('Digite o comprimento da altura do triângulo retângulo: '))
        area = base*altura/2
        perimetro = base + altura + sqrt(base**2+altura**2)
    else:
        raio = float(input('Digite o comprimento do raio do círculo: '))
        area = pi*raio**2
        perimetro = 2*pi*raio

    if x == 1:
        print('\nO valor da área é: {:.2f}\n'.format(area))
    elif x == 2:
        print('\nO valor do perímetro é: {:.2f}\n'.format(perimetro))
    else:
        print('\nO valor da área é: {:.2f}'.format(area))
        print('O valor do perímetro é: {:.2f}\n'.format(perimetro))



