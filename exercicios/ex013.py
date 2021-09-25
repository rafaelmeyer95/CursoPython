# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário atual?\nR$'))

print('O salário após o aumento de 15% será de R${:.2f}.'.format(salario*1.15))