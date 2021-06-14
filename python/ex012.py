print('{:=^51}'.format(' Exercício 012 '))
p = float(input('Preço do produto: R$ '))
print('\033[31mO preço do produto com desconto de 5% é: R$ {:.2f}\033[m'.format(p*0.95))
