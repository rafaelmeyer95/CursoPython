# Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
# valor monetário formatado

import moeda

preco = int(input("Digite o preço: "))
print(f'A metade de {moeda.moeda(preco)} é R${moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é R${moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco,10))}')