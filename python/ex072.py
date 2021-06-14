print('\033[33m{:-^51}\033[m'.format(' Exercício 072 '))
escrito = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezeoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número \033[33m{escrito[num]}\033[m.')
        break
    print('\033[31mNúmero inválido! \033[m', end='')
