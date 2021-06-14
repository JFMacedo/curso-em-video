def leiaInt(msg):
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


def line(tam=42):
    return '-' * tam


def header(txt, tam=42):
    print(line(tam))
    print(txt.center(tam))
    print(line(tam))


def menu(option):
    header('MENU PRINCIPAL')
    c = 1
    for item in option:
        print(f'\033[32m{c}\033[m - \033[36m{item}\033[m')
        c += 1
    print(line())
    opc = leiaInt('Sua Opção: ')
    return opc
