# Apriomere o exercício anterior, mostrando no final:
# a) A soma de todos os valores pares digitados
# b) A soma dos valores da terceira coluna
# c) O maior valor da segunda linha

matriz = [[1, 2, 3], [4, 5, 6], [0, 0, 0]]
somapares = soma3coluna = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para a posição ({l},{c}): '))
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if c == 2:
            soma3coluna += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]

for l in range(3):
    for c in range(3):
        print(f'({matriz[l][c]:^6})',end=' ')
    print()

print(f'A soma de todos os valores pares é: {somapares}')
print(f'A soma de todos os valores da terceira coluna é: {soma3coluna}')
print(f'O maior valor da segunda linha é: {maior}')