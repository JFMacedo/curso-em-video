print('\033[30m{:=^51}\033[m'.format(' Exercício 031 '))
d = float(input('Qual a distância da viagem? '))
if d <= 200:
    print('\033[33mO valor da passagem será: R$ {:.2f}\033[m'.format(d*0.50))
else:
    print('\033[33mO valor da passagem será: R$ {:.2f}\033[m'.format(d*0.45))
