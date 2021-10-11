# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
# cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas cadastradas
# b) A média de idade
# c) Uma lista com mulheres
# d) Uma lista das pessoas com idade acima da média

dados = dict()
lista = list()
somaidade = 0

while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo [F/M]: '))
    while dados['Sexo'] not in 'MmFf':
        print('Dados inválidos, tente novamente!')
        dados['Sexo'] = str(input('Sexo [F/M]: '))
    dados['Idade'] = int(input('Idade: '))
    somaidade += dados['Idade']
    lista.append(dados.copy())
    continua = str(input('Deseja continuar? [S/N] '))
    while continua not in 'SsNn':
        print('Dados inválidos, tente novamente!')
        continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break

print(f'Total de pessoas cadastradas: {len(lista)}')
print(f'A média de idade é: {somaidade/len(lista):.2f} anos')
print('Lista de mulheres cadastradas:')
for i in range(len(lista)):
    if lista[i]['Sexo'] in 'Ff':
        print(lista[i]['Nome'])
print('Lista de pessoas com idade acima da média:')
for i in range(len(lista)):
    if lista[i]['Idade'] > (somaidade/len(lista)):
        print(lista[i])

