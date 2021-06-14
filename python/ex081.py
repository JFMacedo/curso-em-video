print(f'\033[33m{" Exercício 081 ":-^51}\033[m')
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('\033[31mOpção invalida!\033[m Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('\033[33m-\033[m'*51)
print(f'Você Digitou \033[35m{len(lista)}\033[m elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: \033[35m{lista}\033[m')
if 5 in lista:
    print('\033[32mO valor 5 faz parte da lista\033[m.')
else:
    print('\033[31mO valor 5 não foi encontrado na lista\033[m.')
