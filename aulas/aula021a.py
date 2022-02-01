def fatorial(num=1):    # Caso não seja inserido nenhum parâmetro, o default é 1
    f = 1
    for c in range(num, 0, -1):     # Calculo de fatorial
        f *= c
    return f

f1 = fatorial(5)        # Calcula o fatorial de 5
f2 = fatorial(4)        # Calcula o fatorial de 4
f3 = fatorial()         # Calcula o fatorial de 1 (parâmetro vazio)

print(f'Os resultados são {f1}, {f2} e {f3}')

