print('\033[7;35m{:=^51}\033[m'.format(' Exercício 033 '))
n1 = float(input('\033[30mDigite o 1º valor: \033[m'))
n2 = float(input('\033[30mDigite o 2º valor: \033[m'))
n3 = float(input('\033[30mDigite o 3º valor: \033[m'))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('\033[35mO maior valor digitado é {}'.format(maior))
print('\033[35mO menor valor digitado é {}'.format(menor))
