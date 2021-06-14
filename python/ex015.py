print('{:=^51}'.format(' Exercício 015 '))
d = int(input('Dias com o carro alugado: '))
k = float(input('Kilometros rodados: '))
print('\033[35mA quantidade a pagar é: R$ {:.2f}\033[m'.format(d*60+k*0.15))
