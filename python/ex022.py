from time import sleep
print('{:=^51}'.format(' Exercício 022 '))
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(1)
print('\033[31mSeu nome em letras maiúculas é {}\033[m'.format(nome.upper()))
print('\033[32mSeu nome em letras minúsculas é {}\033[m'.format(nome.lower()))
print('\033[34mSeu nome tem um totas de {} letras\033[m'.format(len(nome)-nome.count(' ')))
print('\033[33mSeu primerio nome é {} e ele tem {} leras\033[m'.format(nome[:nome.find(' ')], nome.find(' ')))
