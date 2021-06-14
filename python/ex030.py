print('\033[30m{:=^51}\033[m'.format(' Exercício 030 '))
n = int(input('\033[34mDigite um número inteiro: \033[m'))
if (n % 2) == 0:
    print('Esse é um número \033[35mPAR\033[m')
else:
    print('O número ${n} é um número \033[35mIMPAR\033[m')
