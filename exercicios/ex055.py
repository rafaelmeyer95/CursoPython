# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = [0] * 5 # Cria um vetor de zeros

for i in range(5):
    peso[i] = float(input('Digite o peso da {}ª pessoa: '.format(i+1)))

maior = peso[0]
menor = peso[0]

for i in range(1,5,1):
    if peso[i] > maior:
        maior = peso[i]
    if peso[i] < menor:
        menor = peso[i]
print('O menor valor lido foi {}Kg.'.format(menor))
print('O maior valor lido foi {}Kg.'.format(maior))