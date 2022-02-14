from UtilidadesCeV import moeda

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: "{entrada}" é um preço inválido')
        else:
            valido = True
            return float(entrada)

def resumo(valor, aumento, desconto):
    print(50 * '=')
    print('Resumo do valor'.center(50).upper())
    print(50 * '=')
    print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}'.center(50))
    print(f'O dobro de {moeda.moeda(valor)}  é {moeda.moeda(moeda.dobro(valor))}'.center(50))
    print(f'{moeda.moeda(valor)} com {aumento}% de aumento é {moeda.moeda(moeda.aumentar(valor, aumento))}'.center(50))
    print(f'{moeda.moeda(valor)} com {desconto}% de desconto é {moeda.moeda(moeda.diminuir(valor, desconto))}'.center(50))
    print(50 * '=')