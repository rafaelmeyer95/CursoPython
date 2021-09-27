# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200 Km e R$0,45 para viagens mais longas.

dist = float(input('Qual a distância da viagem em Km?\n'))

if dist<=200:
    valor = 0.50 * dist
else:
    valor = 0.45 * dist

print("O valor da passagem é R${:.2f}!".format(valor))

'''Maneira que o professor resolve:

valor = dist * 0.50 if dist <= 200 else dist * 0.45

'''