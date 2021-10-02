# Melhore o jogo do exercício 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tentativas = 1
maquina = randint(0,10)

jogador = int(input('Estou pensando em um número de 0 a 10, tente adivinhar qual é: '))

while jogador != maquina:
    if jogador < maquina:
        jogador = int(input('É maior, tente novamente: '))
        tentativas += 1
    else:
        jogador = int(input('É menor, tenta novamente: '))
        tentativas += 1

print('\nAcertou mizeravi!\nN° de tentativas: {}.'.format(tentativas))

