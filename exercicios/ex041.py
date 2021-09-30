#  A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: Master

from datetime import date

nasc = int(input('Insira o ano de nascimento: '))
idade = date.today().year-nasc

if idade <= 9:
    print ('O atleta possui {} anos e pertence a categoria Mirim'.format(idade))
elif idade <= 14:
    print ('O atleta possui {} anos e pertence a categoria Infantil'.format(idade))
elif idade <= 19:
    print ('O atleta possui {} anos e pertence a categoria Junior'.format(idade))
elif idade <= 25:
    print ('O atleta possui {} anos e pertence a categoria Senior'.format(idade))
else:
    print ('O atleta possui {} anos e pertence a categoria Master'.format(idade))