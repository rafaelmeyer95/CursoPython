p1 = float(input('Nota da primeira prova: '))
p2 = float(input('Nota da segunda prova: '))
p3 = float(input('Nota da terceira prova: '))
p4 = float(input('Nota da quarta prova: '))

media = (p1+p2+p3+p4)/4

if media < 7:
    print('Sua média foi {:.2f}, estude mais!'.format(media))
else:
    print('Sua média foi {:.2f}, parabéns!'.format(media))
