# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares

numeros = (int(input("Digite o primeiro número: ")),
           int(input("Digite o segundo número: ")),
           int(input("Digite o terceiro número: ")),
           int(input("Digite o quarto número: ")))

print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O número 3 foi digitado pela primeira vez na posição {numeros.index(3)+1}')
else:
    print('O número 3 não foi digitado nenhuma vez')
print('Os números pares são: ',end='')
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i],end=' ')
