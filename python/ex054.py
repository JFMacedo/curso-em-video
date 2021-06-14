from datetime import date
cont1 = 0
cont2 = 0
hoje = date.today().year
print('\033[36m{:↔^51}\033[m'.format(' Exercício 054 '))
for c in range(1, 8):
    ano = int(input('Ano de nascimento {}ª pessoa: '.format(c)))
    if hoje - ano >= 18:
        cont1 = cont1+1
    else:
        cont2 = cont2+1
print('\nAo todo tivemos \033[33m{}\033[m pessoas maiores de idade.'.format(cont1))
print('E tombém tivemos \033[33m{}\033[m pessoas menores de idade.'.format(cont2))
