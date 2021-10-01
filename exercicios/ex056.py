# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.

soma = 0
idadevelho = 0
mjovem = 0
nomevelho = ''

for i in range(1,5,1):
    print(40*'-')
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i)))
    idade = int(input('Digite da idade da {}ª pessoa: '.format(i)))
    sexo = str(input('Digite o sexo da {}ª pessoa [F/M]: '.format(i)))
    soma += idade
    if sexo in 'Mm':
        if idade > idadevelho:
            nomevelho = nome
            idadevelho = idade
    if sexo in 'Ff':
        if idade < 20:
            mjovem += 1

media = soma / 4

print('\nA média de idade é {:.2f}'.format(media))
if nomevelho == '':
    print('Não há pessoas do sexo masculino ')
else:
    print('O homem mais velho é o {}'.format(nomevelho))
print('{} mulheres tem menos de 20 anos'.format(mjovem))

