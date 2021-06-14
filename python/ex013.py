print('{:=^51}'.format(' Exercício 013 '))
s = float(input('Quanto é seu salário? R$ '))
print('\033[7;33mSeu salário com aumento de 15% seria: R$ {:.2f}\033[m'.format(s*1.15))
