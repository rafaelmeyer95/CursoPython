#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip().title()
separado = nome.split()

print("Olá {},".format(nome))
print('Seu primeiro nome é {}.'.format(separado[0]))
print('Seu último nome é {}'.format(separado[len(separado)-1]))