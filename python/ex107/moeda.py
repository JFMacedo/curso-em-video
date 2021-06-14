def aumentar(preco, taxa):
    tot = preco * taxa/100 + preco
    return tot


def diminuir(preco, taxa):
    tot = preco + preco * taxa/100
    return tot


def dobro(preco):
    tot = preco*2
    return tot


def metade(preco):
    tot = preco/2
    return tot
