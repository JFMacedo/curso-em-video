print('{:=^51}'.format(' Exercício 006 '))
n = float(input('Digite um numero: '))
print('\033[7;30mSeu dobro é: {}\033[m\nSeu triplo é: {}\n\033[4;32mSua raiz quadrada é: {:.2f}\033[m'.format(n*2, n*3, n**(1/2)))
