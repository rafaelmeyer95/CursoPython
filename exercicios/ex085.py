# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]

for i in range (7):
    num = (int(input(f'Digite o {i+1}º número: ')))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()
print(f'\nOs números pares digitados foram: {lista[0]}')
print(f'Os números ímpares digitados foram: {lista[1]}')
