# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = float(input('Digite um número: '))
print('O dobro de {0} é {1}.\nO triplo de {0} é {2}.\nA raíz quadrada de {0} é {3:.3f}.'.format(num,2*num,3*num,num**(1/2)))
