print('\033[34m{:x^51}\033[m'.format(' Ecercício 065 '))
sn = 'S'
maior = menor = cont = total = 0
while sn == 'S':
    num = float(input('Digite um número: '))
    sn = str(input('Quer continuar? [\033[32mS\033[m/\033[31mN\033[m] ')).strip().upper()[0]
    total = total + num
    cont = cont + 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print('Você digitou \033[34m{:.0f} números\033[m e a média foi \033[34m{:.2f}\033[m.'.format(cont, total/cont))
print('O maior valor foi \033[34m{:.2f}\033[m e o menor foi \033[34m{:.2f}\033[m.'.format(maior, menor))
