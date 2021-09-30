# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário          2 para octal          3 para hexadecimal

num = int(input('Digite um número inteiro: '))

print('Qual tipo de conversão?\n(1) Binário\n(2) Octal\n(3) Hexadecimal')

conversao = int(input())

if conversao == 1:
    print('O número {} em binário é: {}'.format(num,bin(num)[2:]))
elif conversao == 2:
    print('O número {} em otcal é: {}'.format(num, oct(num)[2:]))
elif conversao == 3:
    print('O número {} em binário é: {}'.format(num, hex(num)[2:].upper()))
else:
    print('Opção inválida!')
