print('{:=^51}'.format(' Exercício 008 '))
m = float(input('Valor em metros: '))
print('\033[30;42mValor em centímetros: {}\033[m\n\033[7;33mValor em milímetros: {}\033[m'.format(int(m*100), int(m*1000)))
