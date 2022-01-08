#

def numeros(*num):
    maior = 0
    for i in num:
        if i > maior:
            maior = i
    print(f"De todos os {len(num)} números, o maior é o {maior}.")


numeros(2,9,4,5,7,1)
numeros(4,7,0)
numeros(1,2)
numeros(6)
numeros()