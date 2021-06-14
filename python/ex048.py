soma = 0
cont = 0
print('\033[33m{:•^49}\033[m'.format(' Exercício 048 '))
for c in range(1, 1150, 2):
    if c % 3 ==0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos os \033[33m{}\033[m valores solicitados é \033[33m{}\033[m'.format(cont, soma))
