# Refaça o exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

a = float(input('Digite o comprimento do primeiro vértice: '))
b = float(input('Digite o comprimento do segundo vértice: '))
c = float(input('Digite o comprimento do terceiro vértice: '))

if a + b < c or a + c < b or b + c < a:
    print('Os valores indicados não podem formar um triângulo')
else:
    if a == b == c:
        print('Os valores indicados podem formar um triângulo equilátero')
    elif a == b or a == c or b == c:
        print('Os valores indicados podem formar um triângulo isósceles')
    else:
        print('Os valores indicados podem formar um triângulo escaleno')