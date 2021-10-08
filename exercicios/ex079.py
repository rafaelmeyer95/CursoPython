# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final,serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
continua = 'S'

while True:
    num = (int(input('Digite um número: ')))
    if num in lista:
        print('Esse número já existe na lista.')
    else:
        lista.append(num)
    continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break

lista.sort()
print(f'Os valores digitados foram: {lista} ')


