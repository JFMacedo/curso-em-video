print(f'\033[33m{" Exercício 094 ":-^51}\033[m')
lista = []
pessoa = {}
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        sexo = str(input('Sexo: ')).strip().upper()
        if sexo not in 'MF':
            print('\033[31mERRO!\033[m Responda apenas M ou F.')
        else:
            break
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resp not in 'SN':
            print('\033[31mERRO!\033[m Responda apenas com S ou N.')
        else:
            break
    if resp == 'N':
        break
print('\033[33m-\033[m'*51)
print(f'\033[35mA)\033[m Ao todo temos \033[34m{len(lista)}\033[m pessoas cadastradas.')
sidade = 0
for i, v in enumerate(lista):
    sidade += lista[i]['Idade']
media = sidade/len(lista)
print(f'\033[35mB)\033[m A média de idade é de \033[34m{media:.2f}\033[m anos.')
print('\033[35mC)\033[m As mulheres cadastradas foram: ', end='')
for c in lista:
    if c['Sexo'] == 'F':
        print(c['Nome'], end=' ')
print()
print('\033[35mD)\033[m Lista de pessoas cadastradas que estão acima da média:')
for i, v in enumerate(lista):
    if lista[i]['Idade'] > media:
        for k, v in lista[i].items():
            print(f'   {k} = {v}', end=';')
        print()
print(f'\033[33m{" FIM DO PROGRAMA ":-^51}\033[m')
