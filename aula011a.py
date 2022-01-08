nome = str(input('Digite seu nome: '))
texto = int(input('Escolha uma cor para o texto:\n1 - Vermelho\n2 - Verde\n3 - Amarelo\n4 - Azul\n5 - Roxo\n'))

corestexto = ['\033[31m',
              '\033[32m',
              '\033[33m',
              '\033[34m',
              '\033[35m']

cortexto = corestexto[texto-1]


print('{}{}\033[m'.format(cortexto,nome))

