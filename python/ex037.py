print('{:=^51}'.format(' Exercício 037 '))
num = int(input('\033[35mDigite um numero inteiro: \033[m'))
print('''\033[33mEscolha uma das bases para conversão:
| 1 | Converter para BINÁRIO
| 2 | Converter para OCTAL
| 3 | Converter para HEXADECIMAL\033[m''')
esc = int(input('\033[30mDigite sua escolha: \033[m'))
if esc == 1:
    print('\033[36m{} convertido em BINÁRIO é {}\033[m'.format(num, bin(num)[2:]))
elif esc == 2:
    print('\033[36m{} convertido em OCTAL é {}\033[m'.format(num, oct(num)[2:]))
elif esc == 3:
    print('\033[36m{} convertido em HEXADECIMAL é {}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção errada tente novamente!\033[m')
