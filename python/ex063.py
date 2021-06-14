print('\033[35m{:x^51}\033[m'.format(' Exercício 063 '))
numero = int(input('Quantos termos você quer exibir: '))
termo1 = 0
termo2 = 1
cont = 3
print('\033[34m{}\033[m → \033[34m{}\033[m → '.format(termo1, termo2), end='')
while cont <= numero:
    termo3 = termo1+termo2
    print('\033[34m{}\033[m → '.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont = cont+1
print('\033[35mFIM\033[m')
