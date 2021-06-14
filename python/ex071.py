print('\033[33m{:-^51}\033[m'.format(' Exercício 071 '))
print('{:^51}'.format('CAIXA ELETRONICO JFM'))
print('\033[33m-\033[m'*51)
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
cedula = 100
cont = 0
while True:
    if total >= cedula:
        total -= cedula
        cont += 1
    else:
        if cont > 0:
            print(f'Total de \033[33m{cont} cédulas\033[m de \033[33mR$ {cedula:.2f}\033[m')
        cont = 0
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        if total == 0:
            break
print('\033[33m-\033[m'*51)
print('\033[32m{:^51}\033[m'.format('Volte sempre ao BANCO JFM'))
