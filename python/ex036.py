from time import sleep
print('{:=^51}'.format(' Exercício 036 '))
valorcasa = float(input('\033[34mDigite o valor da casa a ser comprada: \033[m'))
salario = float(input('\033[34mDigite seu salário: \033[m'))
anos = float(input('\033[34mDigite em quantos anos você irá pagar: \033[m'))
mensalidade = valorcasa / (anos*12)
print('\033[35mPROCESSANDO...\033[m')
sleep(1)
if mensalidade > (salario*0.30):
    print('\033[31mO valor da parcela será R$ {:.2f}, e de acordo com seu salário de R$ {:.2f} infelizmente seu financiamento foi NEGADO!\033[m'.format(mensalidade, salario))
else:
    print('\033[33mO valor da parcela será R$ {:.2f}, e de acordo com seu salário de RS {:.2f} seu financiamento foi APROVADO!\033[m'.format(mensalidade, salario))
