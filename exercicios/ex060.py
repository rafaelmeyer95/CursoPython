# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

num = fat = int(input('Digite um número: '))

for i in range(fat-1,1,-1):
    fat = fat*(i)
print('{}! = '.format(num),end='')
for i in range(num,1,-1):
    print('{} x '.format(i),end='')
print ('1 = {}'.format(fat))
