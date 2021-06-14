def moeda(valor, moeda='R$'):
    resp = (f'{moeda} {valor:.2f}'.replace('.', ','))
    return resp


def aumentar(preco=0, taxa=0):
    tot = preco * taxa/100 + preco
    return tot


def diminuir(preco=0, taxa=0):
    tot = preco + preco * taxa/100
    return tot


def dobro(preco=0):
    tot = preco*2
    return tot


def metade(preco=0):
    tot = preco/2
    return tot
