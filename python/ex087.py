print(f'\033[34m{" Exercício 086 ":-^51}\033[m')
somapar = somaco3 = 0
matriz = [[], [], []]
for m in range(0, 3):
    for l in range(0, 3):
        matriz[m].append(int(input(f'Digite um valor para [{m}, {l}]: ')))
print('\033[34m-\033[m'*51)
for m in range(0, 3):
    somaco3 += matriz[m][2]
    maior2 = max(matriz[1])
    for l in range(0, 3):
        if matriz[m][l] % 2 == 0:
            somapar += matriz[m][l]
        print(f'[\033[33m{matriz[m][l]:^5}\033[m]', end='')
    print()
print('\033[34m-\033[m'*51)
print(f'A soma de todos os valores pares é: \033[33m{somapar}\033[m')
print(f'A soma de todos os valores da 3ª coluna é: \033[33m{somaco3}\033[m')
print(f'O maior valor digitado na linha 2 é: \033[33m{maior2}\033[m')
