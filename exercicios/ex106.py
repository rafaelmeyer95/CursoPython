# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

palavra = 'oi'
while palavra.upper() != 'FIM':
    print('~' * 40)
    print('SISTEMA DE AJUDA PyHELP'.center(40))
    print('~' * 40)
    palavra = str(input("Função ou Biblioteca> "))
    if palavra.upper() == 'FIM':
        break
    else:
        print(help(palavra))
