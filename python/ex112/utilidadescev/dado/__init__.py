def leiadinheiro(valor):
    ok = False
    while not ok:
        preco = str(input(valor)).strip().replace(',', '.')
        if preco.isalpha() or preco == '':
            print(f'\033[31mERRO: "{preco}" não é um preço valido!\033[m')
        else:
            ok = True
            return float(preco)


def leiaint(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            n = int(num)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return n