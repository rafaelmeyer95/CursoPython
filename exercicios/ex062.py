# Melhore o exercício 061, perguntando ao usuário se ele quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 termos.

print(37*'=')
print('CALCULANDO UMA PROGRESSÃO ARITMÉTICA')
print(37*'=')

prim = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
continua = 10
result = prim
c=0

while continua != 0:
    for i in range(continua):
        print('{} ➝ '.format(result),end='')
        result += razao
        c += 1
    print('PAUSA')
    continua = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão Aritmética Finalizada com {} termos mostrados!'.format(c))
