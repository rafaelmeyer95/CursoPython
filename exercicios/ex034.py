# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o seu salário atual: R$'))

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

print('O valor do aumento é de R${:.2f}'.format(aumento))