# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo [F/M]: '))

while sexo not in 'MmFf' or sexo in '':
        sexo = str(input('Entrada inválida, tente novamente: '))
print('Sexo {} cadastrado com sucesso!'.format(sexo.upper()))
