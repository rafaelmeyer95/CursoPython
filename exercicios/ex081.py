# Crie um programa que leia vários números e coloque em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente
# c) Se o valor 5 foi digitado e está ou não na lista

lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar? [S/N] '))
    if continua in 'Nn':
        break

lista.sort(reverse=True)
print(f'\nVocê digitou {len(lista)} numeros.')
print(f'Os números digitados, em ordem decrescente é: {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
