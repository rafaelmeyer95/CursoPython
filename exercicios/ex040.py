# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperação
# Média 7.0 ou superior: Aprovado

p1 = float(input('Digite a nota da primeira prova: '))
p2 = float(input('Digite a nota da segunda prova: '))

media = round(((p1+p2)/2),1)

print('Sua média foi {}'.format(media))

if media < 5:
    print('Você foi reprovado')
elif media < 7:
    print('Você está de recuperação')
else:
    print('Você foi aprovado')