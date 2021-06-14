print('\033[35m{:-^51}\033[m'.format(' Exercício 076 '))
print('\033[36m{:^51}\033[m'.format('LISTA DE PREÇOS'))
print('\033[35m-\033[m'*51)
lista = ('G.R. Click 2.4', 534, 'G.R. Havana Star 6.3', 567, 'G.R. Gold 5.3', 558,
     'G.R. Imaginare 06 Pts', 905, 'G.R. Napoles 8.4', 800, 'Comoda Havana Master', 336,
     'Comoda Madri 1.7', 625, 'Criado Havana Plus', 100, 'Criado Mudo Conect', 173)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print('\033[36m{:.<42}'.format(lista[item]), end='')
    else:
        print('R$', '{:>6.2f}\033[m'.format(lista[item]))
print('\033[35m-\033[m'*51)
