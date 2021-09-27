#Crie um programa que eia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = str(input('Qual a cidade que você nasceu?\n'))

cidade = cidade.split()
cidade[0] = cidade[0].capitalize()

print('Santo' in cidade[0])

"""Maneira que o professor resolveu:

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5.upper() == 'SANTO')

"""

