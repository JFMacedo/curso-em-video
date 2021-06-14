from random import randint
print('\033[36m{:-^51}\033[m'.format(' Exercício 068 '))
print('{:^51}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
print('\033[36m-\033[m'*51)
cont = 0
while True:
    pc = randint(0, 10)
    jg = int(input('Digite um valor: '))
    if (pc+jg) % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    pi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print('\033[36m-\033[m'*51)
    print(f'Você jogou {jg} e o computador {pc}. O total {pc+jg} é \033[33m{resultado}\033[m')
    print('\033[36m-\033[m'*51)
    if pi == resultado[0]:
        print('Você \033[32mVENCEU\033[m!')
        cont += 1
        print('Vamos jogar novamente...')
        print('\033[36m-=-\033[m'*17)
    else:
        print('Você \033[31mPERDEU\033[m!')
        break
print('\033[36m-=-\033[m'*17)
print(f'\033[31mGAME OVER\033[m!!! Você venceu {cont} vezes.')
