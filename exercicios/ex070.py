# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# a) Qual é o total gasto na compra
# b) Quantos produtos custam mais de R$1000,00
# c) Qual é o nome do produto mais barato.

soma = caro = 0
menor = barato = ''

print('-' * 35)
print('lojinha do rafa'.upper())
print('-' * 35)

while True:
    continua = str(input('\nDeseja cadastrar um novo produto? [S/N] '))
    if continua in 'Nn':
        break
    if continua in 'Ss':
        produto = str(input('Digite o nome do produto: '))
        preco = float(input('Digite o preço do produto: R$'))
        soma += preco
        if menor == '':
            menor = preco
            barato = produto
        if preco < menor:
            barato = produto
        if preco > 1000:
            caro += 1
    else:
        print('Entrada inválida!')
print (f'Total gasto: {soma}.\n{caro} produtos mais caros que R$1.000,00\nProduto mais barato: {barato}')
