# Crie um programa que tenha uma tupla com todas as contas do apartamento a pagar no mês
# Suponha que você more com mais duas pessoas e divida o valor total igualmente entre os 3

tupla = ('Aluguel',1000,'Luz',279.17,'Internet',100,
         'IPTU',29.70,'Lixo',18.98,'TOTAL',1000+279.17+100+29.70+18.98,
         'Valor Individual',(1000+279.17+100+29.70+18.98)/3)
nome = 'contas ap'
print(40*'-')
print(f'{nome:^40}'.upper())
print(40*'-')
for i in range(0,len(tupla),2):
    print(f'{tupla[i]:.<30}',end='')
    print(f'R${tupla[i+1]:>7.2f}')