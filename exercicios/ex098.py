# Faça um programa que leia uma função chamada "contador" que receba três parâmetros (inicio, fim, passo). Seu
# programa tem que realizar contagens através da função criada:
# De 1 até 10, de 1 em 1
# De 10 até 0, de 2 em 2
# Uma contagem personalizada.

from time import sleep

def contagem(inicio,fim,passo):
    if passo < 0:
        passo = passo*(-1)
    elif passo == 0:
        passo = 1

    print("=-"*20)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}:")
    sleep(3)

    if inicio > fim:
        if passo < inicio - fim:
            for i in range(((inicio - fim) // passo) + 1):
                print(f"{inicio - i * passo} ", end="", flush=True)
                sleep(.5)
            print('Fim')
        else:
            print("O valor do passo é muito grande")

    elif fim > inicio:
        if passo < fim-inicio:
            for i in range (((fim-inicio)//passo)+1):
                print(f"{inicio+i*passo} ",end="", flush=True)
                sleep(.5)
            print('Fim')
        else:
            print("O valor do passo é muito grande")

    else:
        print("O valor inicial e final devem ser diferentes")

contagem(0,10,1)
contagem(10,0,2)
i = int(input("Digite o número de início: "))
f = int(input("Digite o número de fim: "))
p = int(input("Digite o passo: "))
contagem(i,f,p)