from time import sleep


def maior(* lista):
    mai = max(lista)
    print('Analisando os valor passados...')
    for n in lista:
        print(f'{n}', end=' ')
        sleep(0.5)
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


def lin():
    print('\033[33m-\033[m'*51)


maior(3, 4, 5, 1, 9, 2, 5)
lin()
maior(4, 1, 5, 2, 0)
lin()
maior(3, 0, 7)
lin()
maior(1, 2)
lin()
maior(4)