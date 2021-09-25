# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Qual o valor atual do produto?\nR$'))

print('Este produto com 5% de desconto custará: R${:.2f}.'.format(valor*.95))
