from random import shuffle
print('{:=^51}'.format(' Exercício 020 '))
n1 = str(input('1ª Pessoa: '))
n2 = str(input('2ª Pessoa: '))
n3 = str(input('3ª Pessoa: '))
n4 = str(input('4ª Pessoa: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de escolha é:')
print(lista)
