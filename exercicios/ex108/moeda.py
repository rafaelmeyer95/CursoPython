def metade(p):
    res = p/2
    return res

def dobro(p):
    res = p*2
    return res

def diminuir(preco, descont):
    res = preco - preco*descont/100
    return res

def aumentar(preco, aument):
    res = preco + preco*aument/100
    return res

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')
