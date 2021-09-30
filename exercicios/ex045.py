#

from random import randint
from time import sleep

itens= ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('Escolha:\n(1) Pedra\n(2) Papel\n(3) Tesoura\n'))
maquina = randint(1,3)

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO\n')
sleep(.5)

print('Você escolheu {} e a máquina escolheu {}!'.format(itens[jogador-1],itens[maquina-1]))

if jogador == maquina:
    print('Resultado: EMPATE!')
elif jogador == 1:
    if maquina == 2:
        print('Resultado: Você perdeu!')
    else:
        print('Resultado: Você ganhou!')
elif jogador == 2:
    if maquina ==1:
        print('Resultado: Você ganhou!')
    else:
        print('Resultado: Você perdeu!')
else:
    if maquina == 1:
        print('Resultado: Você perdeu!')
    else:
        print('Resultado: Você ganhou!')
