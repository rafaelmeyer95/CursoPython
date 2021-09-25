#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Qual é a largura da parede em metros?\n'))
altura = float(input('Qual é a altura da parede em metros?\n'))

print('A área da parede é {:.2f}m² e são necessários {:.2f} litros de tinta para pintá-la.'.format(altura*largura,altura*largura/2))
