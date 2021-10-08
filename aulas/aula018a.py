# Aula 018 - Variável Composta do Tipo Lista (Parte 2)

galera = []
dados = []
maior = menor = 0

for i in range(3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        menor += 1
print(f'No total temos {maior} maiores de idade e {menor} menores de idade.')