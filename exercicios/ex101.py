# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
from datetime import date

def voto(nasc):
    idade = date.today().year - nasc
    if idade < 16:
        return (f'Com {idade} anos: voto NEGADO.')
    elif 16 <= idade < 18 or idade >= 65:
        return (f'Com {idade} anos: voto OPCIONAL.')
    else:
        return (f'Com {idade} anos: voto OBRIGATÓRIO.')

                # Programa Principal
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
