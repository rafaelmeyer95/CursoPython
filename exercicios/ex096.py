# Faça um programa que tenha uma função chamada área que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno

def area(lar,comp):
    a = lar*comp
    print(f"A área de um terreno de {lar}x{comp} é de {a} m².")


l = float(input("Largura do terreno: "))
c = float(input("Comprimento do terreno: "))
area(l,c)
