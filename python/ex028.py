from random import randint
from time import sleep
print('{:=^55}'.format(' Exercicio 031'))
computador = randint(0, 5)
print('\033[34m:•:•:\033[m' * 11)
print('{:-^55}'.format('Vou pensar um numero entre 0 e 5, tente adivinhar'))
print('\033[34m:•:•:\033[m' * 11)
jogador = int(input('Em que numero eu pensei? '))
print('\033[33mPROCESSANDO...\033[m')
sleep(2)
if jogador == computador:
    print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no numero {} e não no {}\033[31m'.format(computador, jogador))