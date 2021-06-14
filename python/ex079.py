print(f'\033[34m{" Exercício 079 ":-^51}\033[m')
lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('\033[32mValor cadastrado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado, não cadastrado!\033[m')
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('\033[31mOpção inválida!\033[m Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('\033[34m-\033[m'*51)
print(f'Você digitou os valores: {sorted(lista)}')
