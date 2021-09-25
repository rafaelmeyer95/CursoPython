# Faça um algoritmo que leia o preço de um produto e a porcentagem de desconto a ser aplicada e
# informe o novo valor

valor = float(input('Qual o valor atual do produto?\nR$'))
desconto = int(input('Qual a porcentagem de desconto a ser aplicada?\n'))

print('Este produto com {}% de desconto custará: R${:.2f}.'.format(desconto,valor*(1-(desconto/100))))