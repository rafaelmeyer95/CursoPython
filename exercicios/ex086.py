# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite um valor para a posição ({j},{i}): '))

for i in range(3):
    for j in range(3):
        print(f'({matriz[i][j]:^5})', end=' ')
    print()