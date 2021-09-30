"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

valor = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o salário do comprador? '))
anos = int (input('Quantos anos de financiamento? '))

mensalidade = valor / (anos*12)

print('\nPara pagar uma casa de R${:.2f} em {} anos, o valor da prestação é R${:.2f}\n'.format(valor,anos,mensalidade))

if mensalidade > 0.3 * salario:
    print("Empréstimo negado!")
else:
    print('Empréstimo concedido')