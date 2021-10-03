# Refaça o exercício 051, lendo  o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando
# a estrutura de repetição while.

print(37*'=')
print('CALCULANDO UMA PROGRESSÃO ARITMÉTICA')
print(37*'=')

prim = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 0

while c < 9:
    print('{} ➝ '.format(prim+(c*razao)),end='')
    c += 1
print('{}'.format(prim+(c*razao)))