# Aula 016 - Variável Composta do Tipo Tupla.

lanche = ('Hambúrguer','Suco','Pizza','Pudim') # Cria a variável composta 'lanche' e atribui as respectivas variáveis tipo str
vetor = (0 , 2, 3, 4)                          # Cria a variável composta 'vetor' e atribui as respectivas variáveis tipo int
pessoa = ('Rafael', 26, 'M', 65.5)             # Cria a variável composta 'pessoa' e atribui as respectivas variáveis de vários tipos
vetor2 = vetor + vetor                         # Cria a variável composta 'vetor2' que irá receber (0, 2, 3, 4, 0, 2, 3, 4)
vetor3 = 2*vetor                               # Cria a variável composta 'vetor3' que irá receber (0, 2, 3, 4, 0, 2, 3, 4)

print(vetor3.count(4))       # Retorna a quantidade de vezes que o número 4 aparece dentro da variável 'vetor3'    --> 2
print(vetor3.index(3))       # Retorna a posição em que o número 3 aparece pela primeira vez na variável 'vetor3'  --> 2
print(lanche.count('Suco'))  # Retorna a quantidade de vezes que a str 'Suco' aparece dentro da variável 'lanche'  --> 1
print(lanche)                # Retorna a variável 'lanche' com todos os elementos        --> ('Hambúrguer','Suco','Pizza','Pudim')
print(lanche[2])             # Retorna somente o elemento da posição 2                   --> Pizza
print(lanche[0:3])           # Retorna os elementos da posição 0 até a posição 2         --> ('Hambúrguer','Suco','Pizza')
print(lanche[1:])            # Retorna os elementos da posição 1 até o final             --> ('Suco','Pizza','Pudim')
print(lanche[:3])            # Retorna os elementos da posição inicial até a posição 2   --> ('Hambúrguer','Suco','Pizza')
print(lanche[-1])            # Retorna o último elemento                                 --> Pudim
print(lanche[-2])            # Retorna o penúltimo elemento                              --> Pizza
print(lanche[-3:])           # Retorna os elementos da antipenúltima (terceira, de trás pra frente) posição até a última posição  --> ('Suco','Pizza','Pudim')
print(lanche[:-1])           # Retorna os elementos da posição inicial até a penúltima posição   --> ('Hambúrguer','Suco','Pizza')
print(sorted(lanche))        # Retorna todos os elementos da variável 'lanche' em ordem alfabética
print(sorted(vetor))         # Retorna todos os elementos da variável 'vetor' em ordem crescente


for comida in lanche:                # Roda um loop onde a cada repetição a variável 'comida' assume um elemento da variável composta 'lanche'
    print(f'Eu vou comer {comida}')  # Nessa estrutura não é possível saber a posição de cada elemento.

print('\n')

for cont in range(0, len(lanche)):  # Roda um loop onde a cada repetição a variável 'cont' assume um número inteiro (de 0 até o tamanho da variável 'lanche')
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('\n')

for pos, comida in enumerate(lanche):   # Roda um loop onde a cada repetição a variável 'comida' assume um elemento da variável composta 'lanche' e a variável 'pos' recebe o respectivo índice
    print(f'Eu vou comer {comida} na posição {pos}')