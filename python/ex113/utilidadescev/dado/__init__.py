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
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mERRO! O usuário preferiu não digitar esse número.\033[m')
        else:
            break
    return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mERRO: O usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            break
    return num
