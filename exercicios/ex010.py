#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considerar US$1,00 = R$5,23

num = float(input('Quanto dinheiro você tem na carteira?\nR$'))

print('Você pode comprar {:.2f} doláres.'.format(num/5.23))