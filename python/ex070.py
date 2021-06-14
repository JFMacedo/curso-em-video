print('\033[33m{:-^51}\033[m'.format(' Exercício 070 '))
print('{:^51}'.format('LOJA SUPER BARATÃO'))
print('\033[33m-\033[m'*51)
total = preco1000 = 0
precobarato = 99999999999
nomebarato = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: '))
    total = total+preco
    if preco > 1000:
        preco1000 = preco1000+1
    if preco < precobarato:
        nomebarato = nome
        precobarato = preco
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('{:-^51}'.format(' \033[33mFim do Programa\033[m '))
print(f'O total da compra foi \033[36mR$ {total:.2f}\033[m.')
print(f'Temos \033[36m{preco1000} produtos\033[m custanco mais de R$ 1000.00.')
print(f'O produto mais barato foi \033[36m{nomebarato}\033[m que custa \033[36mR$ {precobarato:.2f}\033[m')
