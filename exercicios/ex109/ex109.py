# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

preco = int(input("Digite o preço: "))
print(f'A metade de {moeda.moeda(preco)} é R${moeda.metade(preco,True)}')
print(f'O dobro de {moeda.moeda(preco)} é R${moeda.dobro(preco,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco,10,True)}')