print('{:=^51}'.format(' Exercício 005 '))
n = int(input('Digite um numero inteiro: '))
print('\033[33mSeu antecessor é: {}\033[m\n\033[7;33mSeu sucessor é: {}\033[m'.format(n-1, n+1))
