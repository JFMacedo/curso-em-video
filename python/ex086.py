print(f'\033[34m{" Exercício 086 ":-^51}\033[m')
matriz = [[], [], []]
for m in range(0, 3):
    for l in range(0, 3):
        matriz[m].append(int(input(f'Digite um valor para [{m}, {l}]: ')))
print('\033[34m-\033[m'*51)
for m in range(0, 3):
    for l in range(0, 3):
        print(f'[\033[33m{matriz[m][l]:^5}\033[m]', end='')
    print()
