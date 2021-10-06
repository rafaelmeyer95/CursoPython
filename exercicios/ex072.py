# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero','um','dois','três','quatro',
           'cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','catorze',
           'quinze','dezesseis','dezessete','dezoito',
           'dezenove','vinte')
while True:
    num = int(input('Digite um número inteiro de 1 a 20: '))
    if 0 <= num <= 20:
        break
    print('Número inválido!')
print(f'Você digitou o número {numeros[num]}.')