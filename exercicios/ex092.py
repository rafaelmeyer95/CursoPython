# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule
# e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
dados = dict()

dados['Nome'] = str(input('Nome: '))
dados['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
dados['CTPF'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['CTPF'] == 0:
    del dados['CTPF']

else:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Contratação'] + 35 ) - (date.today().year - dados['Idade'])

for k,v in dados.items():
    print(f'{k}: {v}')