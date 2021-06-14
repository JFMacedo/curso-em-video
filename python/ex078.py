print(f'\033[33m{" Exercício 078 ":-^36}\033[m')
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(lista)
menor = min(lista)
print('\033[33m-\033[m'*36)
print(f'Você digitou os valor {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, v in enumerate(lista):
    if v == maior:
        print(f'{pos}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'{pos}...', end=' ')
