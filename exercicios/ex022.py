"""Crie um programa que leia o nme completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome  """

nome = str(input('Digite seu nome completo:\n')).strip()

print('Seu nome em maiúsculas é:',nome.upper())
print('Seu nome em minúsculas é:',nome.lower())
print('Seu nome possui {} letras.'.format(len(nome.replace(' ',''))))

lista = nome.split()

print('Seu primeiro nome possui {} letras.'.format(len(lista[0])))

