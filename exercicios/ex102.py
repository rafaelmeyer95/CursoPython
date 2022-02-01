# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial.

def fatorial(num=1,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range (num, 1, -1):
        f *= c
    if show == True:
        for i in range (num-1):
            print(f'{i+1} x',end=" ")
        print(f'{num} =',end=" ")
    print(f)

            # Programa Principal
print(fatorial(4, show=True))
help(fatorial)