# Escreva um programa que eia a velocidade de um carro. Se ele ultrapassar os 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

vel = int(input('Qual a velocidade do carro em Km/h?\n'))

if vel>80:
    print('Você foi multado no valor de R${},00.'.format((vel-80)*7))
else:
    print('Se beber, não dirija!')

