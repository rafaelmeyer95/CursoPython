# Aula sobre condições aninhadas

p1 = float(input('Digite sua nota na primeira prova: '))
p2 = float(input('Digite sua nota na segunda prova: '))
p3 = float(input('Digite sua nota na terceira prova: '))
p4 = float(input('Digite sua nota na quarta prova: '))

media = (p1+p2+p3+p4)/4

if media < 5:
    print('Você precisa estudar muito mais!')
elif media < 7:
    print('Você precisa estudar um pouco mais!')
elif media < 9:
    print('Você está indo bem!')
else:
    print('Parabéns, continue assim!')