print(f'\033[33m{" Exercício 089 ":-^51}\033[m')
lista = []
cont = 0
while True:
    lista.append(list())
    lista[cont].append(str(input('Nome: ')).strip())
    lista[cont].append(list())
    lista[cont][1].append(float(input('1ª nota: ')))
    lista[cont][1].append(float(input('2ª nota: ')))
    lista[cont].append((lista[cont][1][0]+lista[cont][1][1])/2)
    cont += 1
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('\033[31mOpção invalida!\033[m Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('\033[33m-\033[m'*51)
print('\033[34mNo.', f'{"NOME":<41}', f'{"MÉDIA":>5}\033[m')
print('\033[33m-\033[m'*51)
for c in range(0, len(lista)):
    print(f'{c:^3}', f'{lista[c][0]:<41}', f'{lista[c][2]:>5.1f}\033[m')
print('\033[33m-\033[m'*51)
while True:
    op = int(input('Mostrar nota de qual aluno? (\033[31m999 para finalizar\033[m): '))
    if op != 999:
        print(f'Notas de \033[34m{lista[op][0]}\033[m são \033[34m{lista[op][1]}\033[m')
        print('\033[33m-\033[m'*51)
    else:
        print(f'\033[33m{" FIM DO PROGRAMA ":-^51}\033[m')
        break
