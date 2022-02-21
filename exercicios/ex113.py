# Escreva um programa que leia um valor inteiro e um valor real, incluindo a possibilidade
# da digitação de um número de tipo inválido.

erro1 = erro2 = True

while erro1 == True:
    try:
        a = int(input('Digite um número inteiro: '))
    except:
        print('Erro: por favor, digite um número inteiro válido.')
    else:
        erro1 = False

while erro2 == True:
    try:
        b = float(input('Digite um número real: '))
    except:
        print('Erro: por favor, digite um número real válido.')
    else:
        erro2 = False

print(f'O valor inteiro digitado foi {a} e o real foi {b}.')