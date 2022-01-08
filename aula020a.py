# Aula 20 - Funcões (Parte 1)

def contador(* num):
    tam=len(num)
    soma=0
    for i in num:
        soma += i
    print(f'{num} tem {tam} números e a soma deles é {soma}')


contador(2,6,12)
contador(2,5)
contador(4,7,0,12,9,5)

"""def mensagem(texto):
    print('-'*30)
    print()
    print(texto.center(30))
    print()


# Programa Principal
mensagem('Rafael Meyer')
mensagem('Aula 20')
mensagem('Curso de Python')"""