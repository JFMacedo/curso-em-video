print('\033[35m{:•^51}\033[m'.format(' Exercício 066 '))
cont = soma = 0
while True:
    num = float(input('Digite um valor\033[31m [999 para parar]\033[m: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma+num
print(f'A soma dos \033[35m{cont} valores\033[m é \033[35m{soma:.2f}\033[m.')
