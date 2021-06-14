print('\033[33m{:♦^51}\033[m'.format(' Exercício 050 '))
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('\033[30mDigite o {}° número inteiro: \033[m'.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('\033[30mVocê informou {} números PARES a soma deles é \033[33m{}\033[m'.format(cont, soma))
