print(f'\033[36m{" Exercício 082 ":-^51}\033[m')
lista = []
pares = []
impares = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('\033[31mOpção invalida!\033[m Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('\033[36m-\033[m'*51)
print(f'A lista completa é \033[33m{lista}\033[m')
print(f'A lista de pares é \033[33m{pares}\033[m')
print(f'A lista de impares é \033[33m{impares}\033[m')
