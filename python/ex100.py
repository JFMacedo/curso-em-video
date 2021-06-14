from time import sleep
from random import randint


def sorteia(lista):
    for num in range(0, 5):
        lista.append(randint(0, 10))
    print('Sorteando 5 valores para a lista: ', end='')
    for c in numeros:
        print(f'{c}', end=' ')
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    spar = 0
    for c in lista:
        if c % 2 == 0:
            spar += c
    print(f'Somando os valores pares de {lista}, temos {spar}.')


numeros = []
sorteia(numeros)
somapar(numeros)
