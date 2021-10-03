# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, motre quantos números foram digitados e qual foi a soma entre eles (desconsidere o flag).

num = int(input('Digite um número (999 para parar): '))
soma = c = 0

while num !=999:
    soma += num
    c += 1
    num = int(input('Digite um número (999 para parar): '))
print('Foram digitados {} números e a soma entre eles é {}'.format(c,soma))