from random import randint

dinheiro = 100

while True:
    print(f'\nQuantia atual: R${dinheiro:.2f}.')
    valor = float(input('Quanto você quer apostar? R$'))

    while valor > dinheiro:
        print('Você não possui essa quantia.')
        valor = float(input('Quanto você quer apostar? R$'))

    aposta = str(input("""Que tipo de aposta deseja realizar?
    (1) Aposta 1 em 2 - 50% de chance de acerto, lucro de 100%
    (2) Aposta 1 em 3 - 33% de chance de acerto, lucro de 200%
    (3) Aposta 1 em 4 - 25% de chance de acerto, lucro de 300%
    (4) Aposta 1 em 5 - 20% de chance de acerto, lucro de 400%\n"""))

    while aposta not in '1234':
        print('Entrada inválida!')
        aposta = str(input())

    if aposta == '1':
        maquina = randint(1,2)
        jogador = int(input('Digite um valor entre 1 e 2: '))
        while jogador != 1 and jogador != 2:
            print('Entrada inválida!')
            jogador = str(input('Digite um valor entre 1 e 2: '))
        if maquina == jogador:
            dinheiro += valor
            print(f'Você ganhou R${valor:.2f}.')
        else:
            dinheiro -= valor
            print(f'Você Perdeu R${valor:.2f}.')

    elif aposta == '2':
        maquina = randint(1,3)
        jogador = int(input('Digite um valor entre 1 e 3: '))
        while jogador != 1 and jogador != 2 and jogador != 3:
            print('Entrada inválida!')
            jogador = str(input('Digite um valor entre 1 e 3: '))
        if maquina == jogador:
            dinheiro += valor*2
            print(f'Você ganhou R${2*valor:.2f}.')
        else:
            dinheiro -= valor
            print(f'Você Perdeu R${valor:.2f}.')

    elif aposta == '3':
        maquina = randint(1,4)
        jogador = int(input('Digite um valor entre 1 e 4: '))
        while jogador != 1 and jogador != 2 and jogador != 3 and jogador != 4:
            print('Entrada inválida!')
            jogador = str(input('Digite um valor entre 1 e 4: '))
        if maquina == jogador:
            dinheiro += valor*3
            print(f'Você ganhou R${3*valor:.2f}.')
        else:
            dinheiro -= valor
            print(f'Você Perdeu R${valor:.2f}.')

    elif aposta == '4':
        maquina = randint(1,5)
        jogador = int(input('Digite um valor entre 1 e 5: '))
        while jogador != 1 and jogador != 2 and jogador != 3 and jogador != 4 and jogador !=5:
            print('Entrada inválida!')
            jogador = str(input('Digite um valor entre 1 e 5: '))
        if maquina == jogador:
            dinheiro += valor*5
            print(f'Você ganhou R${5*valor:.2f}.')
        else:
            dinheiro -= valor
            print(f'Você Perdeu R${valor:.2f}.')

    if dinheiro == 0:
        print('Você faliu!')
        break

    continua = str(input('Deseja continuar [S/N]? '))
    while continua not in 'SsNn':
        print('Entrada inválida!')
        continua = str(input('Deseja continuar [S/N]? '))

    if continua in 'Nn':
        print(f'Você terminou com R${dinheiro:.2f}.')
        break