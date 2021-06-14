print('\033[35m{:-^51}\033[m'.format(' Exercício 069 '))
print('{:^51}'.format('CADASTRO DE PESSOAS'))
print('\033[35m-\033[m'*51)
cont18 = 0
conth = 0
contm20 = 0
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        cont18 = cont18+1
    sexo = str(input('Sexo: ')).strip().upper()[0]
    if sexo == 'M':
        conth = conth+1
    elif sexo == 'F' and idade < 20:
        contm20 = contm20+1
    print('\033[35m-\033[m'*51)
    prox = str(input('Deseja continuar? ')).strip().upper()[0]
    if prox == 'S':
        print('\033[35m-\033[m' * 51)
    elif prox == 'N':
        break
    else:
        print('Opção Invalida!!!')
print(f'''Total de pessoas com mais de 18 anos: {cont18}.
Ao todo temos {conth} homens cadastrados.
E temos {contm20} mulheres com menos de 20 anos''')
