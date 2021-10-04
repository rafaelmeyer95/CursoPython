from random import randint
from time import sleep

ganhadordoturno = 'jogador'
habilidades = ['Ataque','Defesa','Agilidade','Inteligência','Magia']

print('-'*40+'\nJogo de Cartas no Estilo Super Trunfo\n'+'-'*40+'\n')
dificuldade = int(input('Escolha a dificuldade do jogo:\n(1) Fácil\n(2) Difícil\n'))
regras = input("""
Cada um dos dois jogadores recebe a mesma quantidade de cartas.
Cada carta possui 5 habilidades diferentes (Ataque, Defesa, Agilidade, Inteligência, Magia),
Em cada rodada duas cartas disputam e o vencedor do turno leva as duas cartas.
O vencedor de cada turno escolhe a habilidade a ser disputada no próximo turno.
Em caso de empate alterna o jogador que escolhe a habilidade.
Vence quem ficar com todas as cartas.

Aperte Enter para começar1!
""")

num = int(input('Escolha o número de cartas de cada jogador: '))
cartasjogador = num
cartasmaquina = num

while True:
    jogador = [randint(30, 100) for i in range(5)]
    maquina = [randint(30, 100) for i in range(5)]
    sleep(3)
    print('-'*53)
    print('Você possui {} cartas e o computador possui {} cartas'.format(cartasjogador,cartasmaquina))
    print('\n    Habilidades\nAtaque:         {}\nDefesa:         {}\nAgilidade:      {}\nInteligência:   {}\nMagia:          {}\n'.format(jogador[0],
                                                                                          jogador[1],
                                                                                          jogador[2],
                                                                                          jogador[3],
                                                                                          jogador[4]))
    if ganhadordoturno == 'maquina':
        if dificuldade == 1:
            habilidade = randint(1,5)
        else:
            maior = max(maquina)
            habilidade = maquina.index(maior)+1
        sleep(5)
        print('O oponente escolheu a habilidade: {}'.format(habilidades[habilidade-1]))
        sleep(2)
    else:
        habilidade = int(input('Escolha uma habilidade:\n(1) Ataque\n(2) Defesa\n(3) Agilidade\n(4) Inteligência\n(5) Magia\n'))
        print('Você escolheu a habilidade: {}'.format(habilidades[habilidade - 1]))
    sleep(3)
    if habilidade == 1:
        print('\n              VOCÊ     x   COMPUTADOR\n\033[33mAtaque:        {}      x      {}\033[m\nDefesa:        {}      x      {}\nAgilidade:     {}      x      {}\nInteligência:  {}      x      {}\nMagia:         {}      x      {}\n'.format(jogador[0],
                                                                                                                                            maquina[0],
                                                                                                                                            jogador[1],
                                                                                                                                            maquina[1],
                                                                                                                                            jogador[2],
                                                                                                                                            maquina[2],
                                                                                                                                            jogador[3],
                                                                                                                                            maquina[3],
                                                                                                                                            jogador[4],
                                                                                                                                            maquina[4]))
        sleep(3)
        if jogador[0] < maquina[0]:
            print('\033[31mVOCÊ PERDEU UMA CARTA!\033[m\n')
            cartasjogador += (-1)
            cartasmaquina += 1
            ganhadordoturno = 'maquina'
        elif jogador[0] > maquina[0]:
            print('\033[32mVOCÊ GANHOU UMA CARTA!\033[m\n')
            cartasjogador += 1
            cartasmaquina += (-1)
            ganhadordoturno = 'jogador'
        else:
            print('Empate\n'.upper())
            if ganhadordoturno == 'jogador':
                ganhadordoturno = 'maquina'
            else:
                ganhadordoturno = 'jogador'
    elif habilidade == 2:
        print('\n              VOCÊ     x   COMPUTADOR\nAtaque:        {}      x      {}\n\033[33mDefesa:        {}      x      {}\033[m\nAgilidade:     {}      x      {}\nInteligência:  {}      x      {}\nMagia:         {}      x      {}\n'.format(
                    jogador[0],
                    maquina[0],
                    jogador[1],
                    maquina[1],
                    jogador[2],
                    maquina[2],
                    jogador[3],
                    maquina[3],
                    jogador[4],
                    maquina[4]))
        sleep(3)
        if jogador[1] < maquina[1]:
            print('\033[31mVOCÊ PERDEU UMA CARTA!\033[m\n')
            cartasjogador += (-1)
            cartasmaquina += 1
            ganhadordoturno = 'maquina'
        elif jogador[1] > maquina[1]:
            print('\033[32mVOCÊ GANHOU UMA CARTA!\033[m\n')
            cartasjogador += 1
            cartasmaquina += (-1)
            ganhadordoturno = 'jogador'
        else:
            print('Empate\n'.upper())
            if ganhadordoturno == 'jogador':
                ganhadordoturno = 'maquina'
            else:
                ganhadordoturno = 'jogador'
    elif habilidade == 3:
        print('\n              VOCÊ     x   COMPUTADOR\nAtaque:        {}      x      {}\nDefesa:        {}      x      {}\n\033[33mAgilidade:     {}      x      {}\033[m\nInteligência:  {}      x      {}\nMagia:         {}      x      {}\n'.format(
                    jogador[0],
                    maquina[0],
                    jogador[1],
                    maquina[1],
                    jogador[2],
                    maquina[2],
                    jogador[3],
                    maquina[3],
                    jogador[4],
                    maquina[4]))
        sleep(3)
        if jogador[2] < maquina[2]:
            print('\033[31mVOCÊ PERDEU UMA CARTA!\033[m\n')
            cartasjogador += (-1)
            cartasmaquina += 1
            ganhadordoturno = 'maquina'
        elif jogador[2] > maquina[2]:
            print('\033[32mVOCÊ GANHOU UMA CARTA!\033[m\n')
            cartasjogador += 1
            cartasmaquina += (-1)
            ganhadordoturno = 'jogador'
        else:
            print('Empate\n'.upper())
            if ganhadordoturno == 'jogador':
                ganhadordoturno = 'maquina'
            else:
                ganhadordoturno = 'jogador'
    elif habilidade == 4:
        print('\n              VOCÊ     x   COMPUTADOR\nAtaque:        {}      x      {}\nDefesa:        {}      x      {}\nAgilidade:     {}      x      {}\n\033[33mInteligência:  {}      x      {}\033[m\nMagia:         {}      x      {}\n'.format(
                    jogador[0],
                    maquina[0],
                    jogador[1],
                    maquina[1],
                    jogador[2],
                    maquina[2],
                    jogador[3],
                    maquina[3],
                    jogador[4],
                    maquina[4]))
        sleep(3)
        if jogador[3] < maquina[3]:
            print('\033[31mVOCÊ PERDEU UMA CARTA!\033[m\n')
            cartasjogador += (-1)
            cartasmaquina += 1
            ganhadordoturno = 'maquina'
        elif jogador[3] > maquina[3]:
            print('\033[32mVOCÊ GANHOU UMA CARTA!\033[m\n')
            cartasjogador += 1
            cartasmaquina += (-1)
            ganhadordoturno = 'jogador'
        else:
            print('Empate\n'.upper())
            if ganhadordoturno == 'jogador':
                ganhadordoturno = 'maquina'
            else:
                ganhadordoturno = 'jogador'
    elif habilidade == 5:
        print('\n              VOCÊ     x   COMPUTADOR\nAtaque:        {}      x      {}\nDefesa:        {}      x      {}\nAgilidade:     {}      x      {}\nInteligência:  {}      x      {}\n\033[33mMagia:         {}      x      {}\033[m\n'.format(
                    jogador[0],
                    maquina[0],
                    jogador[1],
                    maquina[1],
                    jogador[2],
                    maquina[2],
                    jogador[3],
                    maquina[3],
                    jogador[4],
                    maquina[4]))
        sleep(3)
        if jogador[4] < maquina[4]:
            print('\033[31mVOCÊ PERDEU UMA CARTA!\033[m\n')
            cartasjogador += (-1)
            cartasmaquina += 1
            ganhadordoturno = 'maquina'
        elif jogador[4] > maquina[4]:
            print('\033[32mVOCÊ GANHOU UMA CARTA!\033[m\n')
            cartasjogador += 1
            cartasmaquina += (-1)
            ganhadordoturno = 'jogador'
        else:
            print('Empate\n'.upper())
            if ganhadordoturno == 'jogador':
                ganhadordoturno = 'maquina'
            else:
                ganhadordoturno = 'jogador'
    if cartasjogador == 0 or cartasmaquina == 0:
        break
if cartasjogador == 0:
    print('\033[7;33;41mVOCÊ PERDEU O JOGO!\033[m')
if cartasmaquina == 0:
    print('\033[7;33;41mVOCÊ GANHOU O JOGO!\033[m')




