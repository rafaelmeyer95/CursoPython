# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.

from datetime import date

menor = 0
maior = 0

for i in range (7):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i+1)))
    if date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print ('{} pessoas são menores de idade\n{} pessoas são maiores de idade'.format(menor,maior))
