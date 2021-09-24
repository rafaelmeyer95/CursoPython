#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

num = float(input('Digite um valor em metros: '))

print('{} metros é equivalente a:\n{} Quilômetros;\n{} centímetros;\n{} milímetros'.format(num,num/1000,num*100,num*1000))