print('\033[36m{:x^51}\033[m'.format(' Exercício 062 '))
termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão: '))
cont = 0
total = 0
prox = 10
while prox != 0:
    total = total+prox
    while cont <= total:
        print('\033[33m{}\033[m'.format(termo), end=' → ')
        termo = termo+razao
        cont = cont+1
    print('\033[36mPAUSA\033[m')
    prox = int(input('Quantos termos você quer mostrar a mais: '))
print('Prograssão finalizado com \033[33m{} termo\033[m exibidos.'.format(total))
