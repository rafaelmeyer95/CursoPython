# Faça o programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa deverá mostrar o tempo
# que falta ou que passou do prazo

from datetime import date


ano = int(input('Informe o ano do seu nascimento: '))

if date.today().year - ano == 18:
    print('Você deve se alistar esse ano')
elif date.today().year - ano < 18:
    print('Você deverá se alistar em {}'.format(ano+18))
else:
    print('Você deveria ter se alistado em {}'.format(ano+18))