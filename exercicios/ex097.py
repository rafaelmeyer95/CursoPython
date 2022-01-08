# Faça uum programa que tenha uma função chamada "escreva", que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável

def mensagem(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(msg.center(tam))
    print('~'*tam)


# Programa principal
mensagem('Rafael')
mensagem('Curso em video de Python')
mensagem('Oi')
