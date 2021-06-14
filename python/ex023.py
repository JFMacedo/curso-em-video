from time import sleep
print('{:=^51}'.format(' Exercício 023 '))
n = int(input('Digite um numero inteiro: '))
print('\033[31mAnalisando o numero {}\033[m'.format(n))
sleep(1)
u = n // 1 % 10
print('\033[34mUnidade: {}\033[m'.format(u))
d = n // 10 % 10
print('\033[34mDezena: {}\033[m'.format(d))
c = n // 100 % 10
print('\033[34mCentena: {}\033[m'.format(c))
m = n // 1000 % 10
print('\033[34mMilhar: {}\033[m'.format(m))
