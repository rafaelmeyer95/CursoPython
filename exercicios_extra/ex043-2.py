# Escreva um programa que leia a altura de uma pessoa e calcule a faixa de peso ideal (IMC entre 18.5 e 25)

altura = float(input('Digite sua altura em metros: '))

imcmin = 18.5
imcmax =  25

pesomin = imcmin*altura**2
pesomax = imcmax*altura**2

print('O peso ideal para você é entre {:.0f}Kg e {:.0f}Kg'.format(pesomin,pesomax))