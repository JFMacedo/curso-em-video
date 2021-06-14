print('\033[7m{:=^51}\033[m'.format(' Exercício 034 '))
s = float(input('Qual p salário do funcionário: R$ '))
if s > 1250:
    print('\033[30mO funcionário que ganhava R$ {:.2f}, passa a ganhar R$ {:.2f}\033[m'.format(s, s*1.10))
else:
    print('\033[30mO funcionário que ganhava R$ {:.2f}, passa a ganhar R$ {:.2f}\033[m'.format(s, s*1.15))
