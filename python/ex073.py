print('\033[32m{:-^51}\033[m'.format(' Exercício 073 '))
time = ('Flamengo', 'Santos', 'Corinthias', 'São Paulo', 'Palmeiras', 'Internacional', 'Atlético-MG', 'Bahia',
        'Athletico-PR', 'Botafogo', 'Grêmio', 'Fortaleza', 'Goiás', 'Ceará', 'Vasco', 'Cruzeiro', 'Chapecoense',
        'Fluminense', 'CSA', 'Avaí')
print(f'\033[34mLista de times do Brasileirão\033[m: {time}')
print('\033[32m-\033[m'*51)
print(f'\033[34mOs 5 primeiros são\033[m: {time[:5]}')
print('\033[32m-\033[m'*51)
print(f'\033[34mOs 4 últimos são\033[m: {time[-4:]}')
print('\033[32m-\033[m'*51)
print(f'\033[34mTimes em ordem alfabética\033[m: {sorted(time)}')
print('\033[32m-\033[m'*51)
print(f'A Chapecoense está na \033[34m{time.index("Chapecoense")+1}ª posição\033[m.')
