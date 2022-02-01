# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do python,
# só que fazendo a validação para aceitar apenas um valor númerico.
# Ex:
# n = leiaInt('Digite um n')

def leiaInt(frase):
    num = input(frase)
    if num.isnumeric():
        return num
    else:
        while not num.isnumeric():
            print("ERRO! Digite um número inteiro válido.")
            num = input("Digite um número: ")
        return num

            # Programa Principal

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')