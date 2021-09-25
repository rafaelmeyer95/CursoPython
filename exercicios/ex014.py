# Escreva um programa que converta uma temperatura digitada em °C para °F

celsius = float(input('Digite a temperatura em graus celsius: '))

print('{:.1f}°C equivale a {:.1f}°F'.format(celsius,((celsius*9/5)+32)))