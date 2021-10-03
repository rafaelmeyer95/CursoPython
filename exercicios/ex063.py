# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci

print('-'*30+'\n'+'Sequência de Fibonacci'+'\n'+'-'*30)

termos = int(input('Quantos termos você quer mostrar? '))
print('~'*30)
print('0 ➝ 1 ➝ ',end='')
ant= 0
atual = 1

while termos !=2:
    prox = ant + atual
    print('{} ➝ '.format(prox),end='')
    ant = atual
    atual = prox
    termos -= 1
print('FIM')