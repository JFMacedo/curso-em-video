def leiaInt(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            n = int(num)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return n


print(f'\033[33m{" Exercício 105 ":-^51}\033[m')
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número \033[32m{n}\033[m')
