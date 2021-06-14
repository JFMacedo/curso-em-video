print('\033[7;35m{:‡^51}\033[m'.format(' Exercício 055 '))
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi de \033[33m{}Kg\033[m.'.format(maior))
print('O menor peso lido foi de \033[33m{}Kg\033[m.'.format(menor))
