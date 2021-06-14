def formato(valor, moeda='R$'):
    """
    → Formata um valor em formatação monetária.
    :param valor: Valor a ser formatado.
    :param moeda: Moeda que será utilizada.
    :return: Valor formatado.
    """
    resp = (f'{moeda} {valor:.2f}'.replace('.', ','))
    return resp


def aumentar(preco=0, taxa=0, formato=False):
    """
    → Aumenta um valor de acordo com a taxa (%) informada.
    :param preco: Valor a ser aplicado a taxa.
    :param taxa: Valor (%) que será aumentado.
    :param formato: Deixa o valor com formatação monetária.
    :return: Valor com aumento, formatado ou não.
    """
    tot = preco * taxa/100 + preco
    if formato:
        return f'R$ {tot:.2f}'.replace('.', ',')
    else:
        return tot


def diminuir(preco=0, taxa=0, formato=False):
    """
    → Diminui um valor de acordo com a taxa (%) informada.
    :param preco: Valor a ser aplicado a taxa.
    :param taxa: Valor (%) que será diminuido.
    :param formato: Deixa o valor com formatação monetária.
    :return: Valor com redução, formatado ou não.
    """
    tot = preco - preco * taxa/100
    if formato:
        return f'R$ {tot:.2f}'.replace('.', ',')
    else:
        return tot


def dobro(preco=0, formato=False):
    """
    → Multiplica um valor por 2.
    :param preco: Valor a ser multiplicado.
    :param formato: Deixa o valor com formatação monetária.
    :return: Dobro do valor.
    """
    tot = preco*2
    if formato:
        return f'R$ {tot:.2f}'.replace('.', ',')
    else:
        return tot


def metade(preco=0, formato=False):
    """
    → Divide um valor por 2
    :param preco: Valor a ser dividido.
    :param formato: Deixa o valor com formatação monetária.
    :return: Metade do valor.
    """
    tot = preco/2
    if formato:
        return f'R$ {tot:.2f}'.replace('.', ',')
    else:
        return tot


def resumo(preco=0, taxaa=0, taxad=0):
    print('\033[33m-'*51)
    print(f'{"RESUMO DE VALORES":^51}')
    print('-'*51)
    print(f'\033[30mPreço analizado: \033[32m\t\t{formato(preco):<15}')
    print(f'\033[30mDobro do preço: \033[32m\t\t{dobro(preco, True):<15}')
    print(f'\033[30mMetade do preço: \033[32m\t\t{metade(preco, True)}')
    print(f'\033[30m{taxaa}% de aumento: \033[32m\t\t{aumentar(preco, taxaa, True)}')
    print(f'\033[30m{taxad}% de redução: \033[32m\t\t{diminuir(preco, taxad, True)}')
