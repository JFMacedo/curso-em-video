from random import randint
print('\033[32m{:-^51}\033[m'.format(' Exercício 074 '))
numero = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ',end='')
for n in numero:
    print(n , end=' ')
print(f'\nO maior valor sorteado foi \033[32m{max(numero)}\033[m.')
print(f'O menor valor sorteado foi \033[32m{min(numero)}\033[m.')
