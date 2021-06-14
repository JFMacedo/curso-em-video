print('\033[33m{:x^51}\033[m'.format(' Exercício 064 '))
num = int(input('Digite um número [\033[31m999 para parar\033[m]: '))
soma = 0
cont = 0
while num != 999:
    soma = soma+num
    num = int(input('Digite um número [\033[31m999 para parar\033[m]: '))
    cont = cont+1
print('Você digitou \033[33m{} valores\033[m e a soma deles é \033[33m{}\033[m.'.format(cont, soma))
