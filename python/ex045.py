from random import randint
from time import sleep
print('\033[36m{:=^51}\033[m'.format(' Exercício 045 '))
escolha = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''\033[30m[0] PEDRA
[1] PAPEL
[2] TESOURA\033[m''')
jg = int(input('\033[35mQual é sua escolha? \033[m'))
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('\033[36m=•=\033[m'*17)
print('''\033[30mComputador escolheu {}
Você escolheu {}\033[m'''.format(escolha[pc], escolha[jg]))
print('\033[36m=•=\033[m'*17)
if pc == 0:
    if jg == 0:
        print('\033[33mEMPATE!\033[m')
    elif jg == 1:
        print('\033[34mVOCÊ GANHOU!\033[m')
    elif jg == 2:
        print('\033[31mCOMPUTADOR GANHOU!\033[m')
    else:
        print('\033[35mOpção inválida!!!\033[m')
elif pc == 1:
    if jg == 0:
        print('\033[31mCOMPUTADOR GANHOU!\033[m')
    elif jg == 1:
        print('\033[33mEMPATE!\033[m')
    elif jg == 2:
        print('\033[34mVOCÊ GANHOU!\033[m')
    else:
        print('\033[35mOpção inválida!!!\033[m')
elif pc == 2:
    if jg == 0:
        print('\033[34mVOCÊ GANHOU!\033[m')
    elif jg == 1:
        print('\033[31mCOMPUTADOR GANHOU!\033[m')
    elif jg == 2:
        print('\033[33mEMPATE!\033[m')
    else:
        print('\033[35mOpção inválida!!!\033[m')