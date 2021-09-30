# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condições de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor do produto? R$'))
print("""\nQual a forma de pagamento?\n
(1) à vista dinheiro/cheque (10% de desconto)
(2) à vista no cartão (5% de desconto)
(3) Até 2x no cartão
(4) 3x ou mais no cartão (20% de juros)""")

x = int(input())

if x == 1:
    print('O valor a ser pago é {:.2f}'.format(valor*.9))
elif x == 2:
    print('O valor a ser pago é {:.2f}'.format(valor*.95))
elif x == 3:
    print("""Em quantas vezes deseja parcelar?
1 x {:.2f}
2 x {:.2f}""".format(valor,valor/2))
elif x == 4:
    print('Em quantas vezes deseja parcelar?')
    for i in range(18):
        print('{} x R${:.2f}'.format(i+3,(valor*1.2)/(i+3)))
else:
    print('Valor inválido!')

