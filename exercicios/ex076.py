# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular

tupla = ('Mouse',30,'Teclado',50,'Monitor',500,'Celular',1500,'Computador',2000,'Notebook',3000)
nome = 'loja do rafa'
print(40*'-')
print(f'{nome:^40}'.upper())
print(40*'-')
for i in range(0,len(tupla),2):
    print(f'{tupla[i]:.<30}',end='')
    print(f'R${tupla[i+1]:>8.2f}')