print('\033[7;33m{:=^51}\033[m'.format(' Exercício 038 '))
num1 = float(input('\033[33mPrimeiro número: \033[m'))
num2 = float(input('\033[33mSegundo número: \033[m'))
if num1 > num2:
    print('\033[34mO PRIMEIRO número é maior!\033[m')
elif num2 > num1:
    print('\033[34mO SEGUNDO número é maior!\033[m')
else:
    print('\033[35mOs dois são IGUAIS\033[m')
