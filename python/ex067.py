print('\033[32m{:-^51}\033[m'.format(' Exercício 067 '))
print('{:^51}'.format('TABUADA'))
while True:
    print('\033[32m-\033[m' * 51)
    num = int(input('Digite um número para tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'\033[36m{num}\033[m x \033[36m{c:2}\033[m = \033[32m{num*c:2}\033[m')
print('\nPrograma de tabuada \033[31mFINALIZADO\033[m!')
