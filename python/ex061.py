print('\033[32m{:+^51}\033[m'.format(' Exercício 061 '))
print('{:^51}'.format('Gerador de PA'))
print('\033[32m+\033[m'*51)
term1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
while cont <= 10:
    cont = cont+1
    print('\033[33m{}\033[m → '.format(term1), end='')
    term1 = term1 + razao
print('\033[33mFIM\033[m')
