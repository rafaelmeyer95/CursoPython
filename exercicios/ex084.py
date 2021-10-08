# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) Uma listagem com as pessoas mais pesadas
# c) Uma listagem com as pessoas mais leves

galera = []
pessoa = []
leves = []
pesadas = []

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        elif pessoa[1] < menor:
            menor = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break

print(f'\nForam cadastradas {len(galera)} pessoas.')

for p in galera:
    if p[1] == menor:
        leves.append(p[0])
print(f'O menor peso cadastrado foi {menor}. Pessoas mais leves: {leves}')

for p in galera:
    if p[1] == maior:
        pesadas.append(p[0])
print(f'O maior peso cadastrado foi {maior}. Pessoas mais pesadas: {pesadas} ')
