print('\033[33m{:•^51}\033[m'.format(' Exercício 057 '))
sexo = str(input('\033[30mInforme seu sexo [M/F]: \033[m')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[31mDados Inválidos!\033[30m Por favor, informe seu sexo [M/F]: \033[m')).strip().upper()[0]
if sexo == 'M':
    print('Sexo \033[33mMASCULINO\033[m registrado com sucesso.')
else:
    print('Sexo \033[33mFEMININO\033[m registrado com sucesso.')
