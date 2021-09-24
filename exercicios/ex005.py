#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))
print('O antecessor de {0} é {1}.\nO sucessor de {0} é {2}.'.format(num,num-1,num+1))