from datetime import date
print('\033[33m{:=^51}\033[m'.format(' Exercício 039 '))
nasc = int(input('Ano de nascimento: '))
hoje = date.today().year
print('Quem nasceu em {} tem \033[33m{} anos\033[m em {}.'.format(nasc, hoje-nasc, hoje))
if (hoje-nasc) < 18:
    print('Ainda faltam \033[33m{} anos\033[m para o alistamento.\nSeu alistamento será em \033[33m{}\033[m.'.format(18-(hoje-nasc), nasc+18))
elif (hoje-nasc) > 18:
    print('Você já deveria ter se alistado há \033[33m{} anos\033[m.\nSeu alistamento foi em \033[33m{}\033[m.'.format((hoje-nasc)-18, nasc+18))
elif (hoje-nasc) == 18:
    print('Você deve se alistar \033[33mIMEDIATAMENTE!\033[m')