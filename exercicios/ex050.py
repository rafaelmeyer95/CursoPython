# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

cont = 0
soma = 0
for i in range(1,7,1):
    num = int(input('Digite o {}° número: '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números pares e a soma deles é {}.'.format(cont,soma))