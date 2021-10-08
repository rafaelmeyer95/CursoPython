# Crie um programa que leia vários números e coloque em uma lista. Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
pares = list()
impares = list()

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 1:
        impares.append(num)
    else:
        pares.append(num)
    continua = str(input('Você quer continuar? [S/N] '))
    if continua in 'Nn':
        break
print(f'Os números digitados foram: {lista}.\n Os números pares são: {pares}.\n Os números ímpares são: {impares}.')