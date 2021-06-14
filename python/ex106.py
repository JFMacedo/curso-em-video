def ajuda():
    from time import sleep
    while True:
        print('\033[32m-'*25)
        print(' SISTEMA DE AJUDA PyHELP')
        print('-'*25)
        resp = str(input('\033[mFunção ou Biblioteca: ')).strip().lower()
        if resp == 'fim':
            print('\033[31m-'*11)
            print(' ATÉ LOGO!')
            print('-'*11)
            break
        print('\033[34m-'*(32+len(resp)))
        print(f' Acessando o manual do comando {resp}')
        print('-'*(32+len(resp)))
        print('\033[35m')
        sleep(1)
        print(help(resp))
        sleep(1)


print(f'\033[33m{" Exercício 106 ":-^51}\033[m')
ajuda()
