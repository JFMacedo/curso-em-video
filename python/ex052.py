print('\033[32m{:•^51}\033[m'.format(' Exercício 052 '))
cont = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end=' ')
        cont = cont + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\033[30m\nO número {} foi divisível {} vezes.'.format(num, cont))
if cont == 2:
    print('Por isso ele \033[34mÉ PRIMO\033[m!')
else:
    print('Por isso ele \033[31mNÃO É PRIMO\033[m')