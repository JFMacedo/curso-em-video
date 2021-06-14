from datetime import date
print('\033[34m{:=^51}\033[m'.format(' Exercício 041 '))
nasc = int(input('Ano de nescimento: '))
hoje = date.today().year
idade = hoje - nasc
print('Nascidos em {} tem {} anos em {}.'.format(nasc, idade, hoje))
if idade <= 9:
    print('Categoria: \033[34mMIRIM\033[m')
elif idade <= 14:
    print('Categoria: \033[34mINFANTIL\033[34m')
elif idade <= 19:
    print('Categora: \033[34mJUNIOR\033[m')
elif idade <= 30:
    print('Categoria: \033[34mADULTO\033[m')
elif idade > 30:
    print('Categoria: \033[34mSENIOR\033[m')
