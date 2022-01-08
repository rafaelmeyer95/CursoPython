# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e Somapar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
# os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    for i in range (0,5):
        lista.append(randint(0,20))
    print(lista)

def Somapar(lis):
    soma = 0
    for i in lis:
        if i % 2 == 0:
            soma += i
    print(f"A soma dos valores pares é {soma}.")

numeros = list()
sorteia(numeros)
Somapar(numeros)

