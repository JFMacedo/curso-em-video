print('\033[7;32m{:♦^51}\033[m'.format(' Exercício 053 '))
frase = str(input('Digite uma frase: ')).strip().upper()
div = frase.split()
jun = ''.join(div)
inv = ''
for letra in range(len(jun)-1, -1, -1):
    inv += jun[letra]
print('O inverso de {} é {}.'.format(jun, inv))
if inv == jun:
    print('Temos um \033[34mpalímdromo\033[m!')
else:
    print('A frase digitada \033[31mnão é um palíndromo\033[m!')
