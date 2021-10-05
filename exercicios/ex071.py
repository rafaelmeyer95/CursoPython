# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$50,00    R$20,00    R$10,00 e R$1,00.

# O professor resolveu com while mas foram muitas condições e o código ficou muito grande.
# Apesar de ser um exercício voltado a prática do while não achei uma boa aplicação e acabei não utilizando

valor = int(input('Digite o valor a ser sacado: '))
ced50 = valor // 50
ced20 = (valor - (ced50*50))// 20
ced10 = (valor - (ced50*50+ced20*20)) // 10
ced1 = valor - (ced50*50+ced20*20+ced10*10)

print(f'{ced50} cédulas de R$50,00\n{ced20} cédulas de R$20,00\n{ced10} cédulas de R$10,00\n{ced1} cédulas de R$1,00')


