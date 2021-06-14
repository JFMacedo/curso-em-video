print('{:=^51}'.format(' Exercício 014 '))
c = float(input('Temperatura em C°: '))
f = 9*c/5+32
print('\033[7;40m{:.1f}C° equivale a {:.1f}F°\033[m'.format(c, f))
