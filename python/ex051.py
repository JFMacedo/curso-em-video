print('\033[30m{:=^51}\033[m'.format(' Exercício 051 '))
print('\033[35m{:^51}\033[m'.format('10 TERMOS DE UMA PA'))
print('\033[30m=\033[m'*51)
term1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for cont in range(term1, razao*10+term1, razao):
    print('\033[35m', cont, '\033[m', end=' → ')
print('\033[36mACABOU\033[m')
