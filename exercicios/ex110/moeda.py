def metade(preco=0, formato=False):
        res = preco/2
        return moeda(res) if formato else res

def dobro(preco=0,formato=False):
        res = preco*2
        return moeda(res) if formato else res

def diminuir(preco=0, descont=0, formato=False):
        res = preco - preco*descont/100
        return moeda(res) if formato else res

def aumentar(preco=0, aument=0,formato=False):
        res = preco + preco*aument/100
        return moeda(res) if formato else res

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(valor,aumento,desconto):
        print(50*'=')
        print('Resumo do valor'.center(50).upper())
        print(50 * '=')
        print(f'A metade de {moeda(valor)} é {moeda(metade(valor))}'.center(50))
        print(f'O dobro de {moeda(valor)}  é {moeda(dobro(valor))}'.center(50))
        print(f'{moeda(valor)} com {aumento}% de aumento é {moeda(aumentar(valor,aumento))}'.center(50))
        print(f'{moeda(valor)} com {desconto}% de desconto é {moeda(diminuir(valor, desconto))}'.center(50))
        print(50*'=')