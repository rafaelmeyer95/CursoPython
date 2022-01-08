# Aula 19 - Variáveis Compostas: Dicionários

estado = dict()     # Criando um dicionário
brasil = list()     # Criando uma lista

for c in range(3):
    estado['uf'] = str(input('Estado: '))       # Cria o item 'uf' e guarda o valor do input
    estado['sigla'] = str(input('Sigla: '))     # Cria o item 'sigla' e guarda o valor do input
    brasil.append(estado.copy())                # Guarda uma cópia do dicionário estado dentro da lista brasil

for e in brasil:
    print()
    for k,v in e.items():
        print(f'{k} - {v}')
