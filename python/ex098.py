from time import sleep


def contagem(a, b, c):
    if c < 0:
        print(f'Contagem de {a} até {b} de {c * -1} em {c * -1}.')
    else:
        print(f'Contagem de {a} até {b} de {c} em {c}.')
    for num in range(a, b + 1 if b > a else b - 1, c):
        print(f'{num}', end=' ')
        sleep(0.3)
    print('\033[32mFIM\033[m!')


def lin():
    print('\033[33m-\033[m' * 51)


print(f'\033[33m{" Exercício 098 ":-^51}\033[m')
contagem(1, 10, 1)
lin()
contagem(10, 0, -2)
lin()
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
if c == 0:
    c = 1
if c < 0:
    c *= -1
if a > b and c > 0:
    c = c * -1
lin()
contagem(a, b, c)
