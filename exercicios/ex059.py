# Crie um programa que leia dois valores e mostre um menu. Seu programa deverá realizar a operação solicitada em cada caso.
# (1) Somar
# (2) Multiplicar
# (3) Maior
# (4) Novos números
# (5) Sair do Programa

from time import sleep

op = 0
num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

while op != 5:
    sleep(2)
    print(32*'-'+'\nQual operação você deseja realizar?\n(1) Soma\n(2) Multiplicação\n(3) Maior\n(4) Novos Números\n(5) Sair do Programa\n '+32*'-')
    op = int(input('Opção Escolhida: '))
    if op == 1:
        print('{} + {} = {}'.format(num1,num2,num1+num2))
    elif op == 2:
        print('{} x {} = {}'.format(num1,num2,num1*num2))
    elif op == 3:
        if num1 > num2:
            print('O maior valor é {}'.format(num1))
        elif num2 > num1:
            print('O maior valor é {}!'.format(num2))
        else:
            print('Os valores são iguais!')
    elif op == 4:
        num1 = int(input('\nDigite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif op ==5:
        print('Encerrando o Programa...')
        sleep(1)
    else:
        print('Valor inválido!')
