# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

div = 2
num = int(input('Digite um número: '))

for i in range(2,num,1):
    if num % i == 0:
        div += 1
if div == 2:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} é divisível por {} números portanto não é primo.'.format(num,div))