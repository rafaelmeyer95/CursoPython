from random import randint
jogador1 = jogador2 = 0

print('\nVez do Jogador 1\n')
while True:
    continuar = str(input('Você quer mais uma carta? [S/N]'))
    if continuar in 'sS':
        num = randint(1,10)
        jogador1 += num
        print(f'Carta: {num}\nTotal: {jogador1}')
        if jogador1 > 21:
            print('Jogador1 Perdeu!')
            break
    elif continuar in 'Nn':
        break
    else:
        print('Entrada inválida.')
if jogador1 < 22:
    print('\nVez do Jogador2\n')
    while True:
        continuar = str(input('Você quer mais uma carta? [S/N]'))
        if continuar in 'sS':
            num = randint(1, 10)
            jogador2 += num
            print(f'Carta: {num}\nTotal: {jogador2}')
            if jogador2 > 21:
                print('Jogador2 Perdeu!')
                break
        elif continuar in 'Nn':
            break
        else:
            print('Entrada inválida.')
if jogador1 < 22 and jogador2< 22:
    if jogador1 > jogador2:
        print('Jogador1 Venceu!')
    elif jogador2 > jogador1:
        print('Jogador2 Venceu')
    else:
        print('Empate')

