from random import randint
from time import sleep
print(f'\033[32m{" Exercício 087 ":-^51}\033[m')
print(f'{"JOGOS DA MEGA SENA":^51}')
print('\033[32m-\033[m'*51)
jogo = []
nj = int(input('Quantos jogos você quer fazer: '))
for n in range(0, nj):
    jogo.append(list())
    while True:
        num = randint(1, 60)
        if num not in jogo[n]:
            jogo[n].append(num)
        if len(jogo[n]) == 6:
            break
    jogo[n].sort()
    print(f'\033[32m{n+1:>2}º jogo: \033[m', end='')
    for p in jogo[n]:
        print(f'[{p:>2}]', end='')
    print()
    sleep(0.5)
print(f'\n\033[32m{" FIM DO PROGRAMA ":-^51}\033[m')
