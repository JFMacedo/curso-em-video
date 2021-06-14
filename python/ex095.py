print(f'\033[33m{" Exercício 095 ":-^51}\033[m')
lista = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    jogador['gols'] = []
    jogador['total'] = 0
    jogador['np'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    for c in range(1, jogador['np']+1):
        jogador['gols'].append(int(input(f'Quantos gols na partida {c}?: ')))
        jogador['total'] += jogador['gols'][-1]
    lista.append(jogador.copy())
    del jogador
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('\033[31mOpção inválida!\033[m Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('\033[33m-\033[m'*51)
print(f'\033[34m{"No.":^5}{"Nome":<27}{"No.Jogos":^10}{"No.Gols":^9}\033[m')
for i, v in enumerate(lista):
    print(f'{i+1:^5}{lista[i]["nome"]:<27}{lista[i]["np"]:^10}{lista[i]["total"]:^9}')
while True:
    print('\033[33m-\033[m'*51)
    op = int(input('Mostrar dados de qual jogador? (\033[31m999 para parar\033[m): '))
    if op <= len(lista):
        print(f'\033[34m{lista[op - 1]["nome"]}\033[m')
        for i, v in enumerate(lista[op-1]['gols']):
            print(f'→ Na partida {i+1}, fez \033[34m{v}\033[m gols.')
        print(f'Foi um total de \033[34m{lista[op-1]["total"]}\033[m de gols.')
    elif op == 999:
        break
    else:
        print(f'\033[31mERRO!\033[m Não existe nenhum jogador com No. {op}! Tente novamente.')
print(f'\033[33m{" Fim do programa ":-^51}')
