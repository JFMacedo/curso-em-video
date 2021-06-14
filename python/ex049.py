print('\033[33m{:•^51}\033[m'.format(' Exercício 049 '))
num = int(input('Digite um numero para ver seu tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = \033[33m{:2}\033[m'.format(num, c, c*num))
