#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número para ver sua tabuada: '))

print('-'*12)

for i in range(10):
    print('{} x {:2} = {}'.format(num,i+1,num*(i+1)))

print('-'*12)


