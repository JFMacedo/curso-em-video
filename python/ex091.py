from time import sleep
from random import randint
from operator import itemgetter
print(f'\033[35m{" Exercício 091 ":-^51}\033[m')
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
print(f'\033[35m{" Ranking ":-^51}\033[m')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    \033[36m{i+1}°\033[m lugar: \033[36m{v[0]}\033[m com {v[1]}')
    sleep(0.5)
