print(f'\033[36m{" Exercício 077 ":-^51}\033[m')
print(f'\033[33m{"VOGAIS NAS PALAVRAS":^51}\033[m')
print('\033[36m-\033[m'*51)
lista = ('JEAN', 'FERNANDES', 'MACEDO', 'JESSICA', 'LAIS', 'CUAGLIO', 'PALMEIRAS', 'NEW', 'ENGLAND', 'PATRIOTS')
for item in lista:
    print(f'\nNa palavra {item}, temos as vogais: ', end='')
    for letra in item:
        if letra.upper() in 'AEIOU':
            print(f'\033[33m{letra}\033[m', end=' ')
print('\n')
print('\033[36m-\033[m'*51)
