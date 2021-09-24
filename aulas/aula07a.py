n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
pot = n1 ** n2

print('A soma entre {0} e {1} é {2}! \nA multiplicação entre {0} e {1} é {3}! \n{0} dividido por {1} é {4:.3f}! \nA divisão inteira de {0} por {1} é {5}! \n{0} elevado a {1} é {6}'.format(n1,n2,soma,mult,div,div_int,pot))

