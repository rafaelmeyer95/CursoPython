# Faça um algoritmo que leia o salário de um funcionário e o aumento, emostre seu novo salário.

salario = float(input('Qual é o salário atual?\nR$'))
aumento = int(input('Qual é a porcentagem de aumento?\n'))

print('O salário após o aumento de {}% será de R${:.2f}.'.format(aumento,salario*(1+(aumento/100))))