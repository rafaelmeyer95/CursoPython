def metade(preco=0, formato=False):
        res = preco/2
        return moeda(res) if formato else res

def dobro(preco=0,formato=False):
        res = preco*2
        return moeda(res) if formato else res

def diminuir(preco=0, descont=0, formato=False):
        res = preco - preco*descont/100
        return moeda(res) if formato else res

def aumentar(preco, aument,formato=False):
        res = preco + preco*aument/100
        return moeda(res) if formato else res

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')
