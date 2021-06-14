from math import hypot
print('{:=^51}'.format(' Exercício 017 '))
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('\033[7;32;40mA medida da hipotenusa é: {:.2f}\033[m'.format(hi))
