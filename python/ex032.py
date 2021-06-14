from datetime import date
print('\033[7;36;40m{:=^51}\033[m'.format(' Exercício 032 '))
ano = int(input('\033[30mDigite um ano para ser analisado (Digite "0" para analisar o ano atual) : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[36mO ano {} é bissexto\033[m'.format(ano))
else:
    print('\033[36mO ano {} não é bissexto\033[m'.format(ano))
