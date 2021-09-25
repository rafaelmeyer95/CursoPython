# O professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

lista = ['nome']*5

for i in range(5):
    lista[i] = str(input('Digite um nome: '))

shuffle(lista)

print('A ordem de apresentação será:\n{}\n{}\n{}\n{}\n{}'.format(lista[0],lista[1],lista[2],lista[3],lista[4]))