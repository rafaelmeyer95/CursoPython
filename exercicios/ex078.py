# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e as suas respectivas posições na lista.

lista = [int(input('Digite um número: '))for i in range(5)]

pmenor = []
pmaior = []
maior = menor = lista[0]
for p,n in enumerate(lista):
    if n <= menor:
        menor = n
    if n>= maior:
        maior = n
for p,n in enumerate(lista):
    if n == menor:
        pmenor.append(p+1)
    if n == maior:
        pmaior.append(p+1)

print(f'O maior valor digitado foi {maior} e aparece nas posições: {pmaior}')
print(f'O menor valor digitado foi {menor} e aparece nas posições: {pmenor}')