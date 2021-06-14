from random import choice
print('{:=^51}'.format(' Exercício 019 '))
n1 = str(input('1ª Pessoa: '))
n2 = str(input('2ª Pessoa: '))
n3 = str(input('3ª Pessoa: '))
n4 = str(input('4ª Pessoa: '))
lista = [n1, n2, n3, n4]
esc = choice(lista)
print('\033[7;34;40mA pessoa escolhida foi: {}\033[m'.format(esc))
