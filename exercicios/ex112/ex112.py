# Dentro do pacote UtilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas
# valores que sejam monetários.

from UtilidadesCeV import dado

preco = dado.leiaDinheiro("Digite o preço: R$")
dado.resumo(preco,20,12)
