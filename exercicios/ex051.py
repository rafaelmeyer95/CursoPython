# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print(37*'=')
print('CALCULANDO UMA PROGRESSÃO ARITMÉTICA')
print(37*'=')

x = int(input('Digite o primeiro termo: '))
y = int(input('Digite a razão: '))

for i in range(10):
    print(x+y*i)