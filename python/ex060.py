print('\033[34m{:-^51}\033[m'.format(' Ecercício 060 '))
num = int(input('Digite um número para calcular seu fatorial: '))
fat = 1
print('\033[33m{}!\033[m \033[34m=\033[m '.format(num), end='')
while num > 0:
    print('{}'.format(num), end='')
    print(' \033[33mx\033[m ' if num > 1 else ' \033[34m=\033[m ', end='')
    fat *= num
    num -= 1
print('\033[32m{}\033[m'.format(fat))
