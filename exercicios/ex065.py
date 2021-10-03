# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores

continua = 's'
soma = c = 0

while continua in 'Ss':
    num = int (input('Digite um número: '))
    if c == 0:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
    soma += num
    c += 1
    continua = str(input('Quer continuar? [S/N] '))
    if continua not in 'SsNn':
        continua = str(input('Desculpe, não entendi!\nQuer continuar? [S/N] '))
media = soma/c
print('Você digitou {} números e a média foi {}.'.format(c,media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior,menor))
