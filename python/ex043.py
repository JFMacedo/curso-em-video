print('\033[34m{:=^51}\033[m'.format(' Exercício 043 '))
peso = float(input('Digite o peso (Kg): '))
altura = float(input('Digite a altura (M): '))
imc = peso / altura ** 2
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[33mABAIXO DO PESO\033[m!')
elif imc <= 25:
    print('PARABÉNS, você está no seu \033[32mPESO IDEAL\033[m!')
elif imc <= 30:
    print('Você está na faixa de \033[36mSOBREPESO\033[m!')
elif imc <= 40:
    print('Você está na feixa de \033[35mOBESIDADE\033[m, ciodado!')
else:
    print('Você está na feixa de \033[31mOBESIDADE MORBIDA\033[m, muito cuidado!')
