print(f'\033[33m{"Exercício 084":-^51}\033[m')
print(f'{"Cadastro de peso":^51}')
print('\033[33m-\033[m' * 51)
lista = []
pessoa = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')).strip())
    peso = float(input('Peso: '))
    pessoa.append(peso)
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
    lista.append(pessoa[:])
    pessoa.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('\033[33m-\033[m' * 51)
print(f'Foram cadastradas \033[33m{len(lista)} pessoas\033[m.')
print(f'O maior peso cadastrado foi \033[33m{maior:.2f}Kg\033[m. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso cadastrado foi \033[33m{menor:.2f}Kg\033[m. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(p[0], end=' ')
