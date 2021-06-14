from random import randint
print('\033[33m{:•^51}\033[m'.format(' Exercício 058 '))
pc = randint(0, 10)
print('Acabei de pansar em um número entre 0 e 10')
jg = int(input('Consegue adivinhar? '))
tentativas = 1
while pc != jg:
    tentativas += 1
    if pc > jg:
        jg = int(input('\033[31mMais...\033[m Tente novamente: '))
    elif pc < jg:
        jg = int(input('\033[31mMenos...\033[m Tente novamente: '))
print('\033[32mPARABÉNS!!!\033[m Você acertou em {} tentativas.'.format(tentativas))
