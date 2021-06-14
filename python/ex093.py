print(f'\033[33m{" Exercício 093 ":-^51}\033[m')
jogador = {}
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
jogador['gols'] = []
jogador['total'] = 0
np = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(1, np+1):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c}?: ')))
    jogador['total'] += jogador['gols'][-1]
print('\033[33m-\033[m'*51)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('\033[33m-\033[m'*51)
print(f'O jogador \033[34m{jogador["nome"]}\033[m jogou {np} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'→ Na partida {i+1}, fez \033[34m{v}\033[m gols.')
print(f'Foi um total de \033[34m{jogador["total"]}\033[m de gols.')
