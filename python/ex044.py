print('\033[34m{:=^51}\033[m'.format(' Exercício 044 '))
preco = float(input('Digite o calor da compra: R$ '))
cond = int(input('''\033[30m[1] À vista no dinheiro/cheque.
[2] À vista no cartão.
[3] Em 2x no cartão.
[4] Em 3x ou mais no cartão.\033[m
\033[34mEscolha a condição de pagamento: \033[m'''))
if cond == 1:
    print('Com essa condição de pagamento você tem \033[33m10% de desconto\033[m.\nO valor da compra será \033[33mR$ '
          '{:.2f}\033[m.'.format(preco*0.90))
elif cond ==2:
    print('Com essa condição de pagamento você tem \033[33m5% de desconto\033[m.\nO valor da compra será \033[33mR$ '
          '{:.2f}\033[m.'.format(preco*0.95))
elif cond == 3:
    print('Você pagará sua compra em \033[33m2x\033[m de \033[33mR$ {:.2f}\033[m, valor total da compra \033[33mR$ '
          '{:.2f}\033[m.'.format(preco/2, preco))
elif cond == 4:
    parc = int(input('\033[34mNúmero de parcelas: \033[m'))
    print('Você pagará sua conta em \033[33m{}x\033[m de \033[33mR$ {:.2f}\033[m, valor total da compra \033[33mR$ '
          '{:.2f}\033[m.'.format(parc, (preco*1.2)/parc, preco*1.2))
