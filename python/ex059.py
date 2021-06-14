from time import sleep
print('\033[33m{:•^51}\033[m'.format(' Exercício 059 '))
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
op =0
while op != 5:
    op = int(input('''\033[36m[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa\033[m
Digite uma opção: '''))
    if op == 1:
        print('A soma entre \033[34m{}\033[m e \033[34m{}\033[m é \033[34m{}\033[m.'.format(n1, n2, n1+n2))
    elif op == 2:
        print('A multiplicação entre \033[34m{}\033[m e \033[34m{}\033[m é \033[34m{}\033[m.'.format(n1, n2, n1*n2))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre \033[34m{}\033[m e \033[34m{}\033[m o maior valor é \033[34m{}\033[m.'.format(n1, n2, maior))
    elif op == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo numero: '))
    elif op == 5:
        print('\033[31mFinalizando...\033[m')
    else:
        print('\033[31mOpção invalida! tente novamente\033[m.')
    sleep(2)
    print('\033[33m•\033[m'*51)
print('Programa finalizado!')