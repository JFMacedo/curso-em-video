from time import sleep
print('\033[7;33m{:=^51}\033[m'.format(' Exercício 026 '))
frase = str(input('Digite uma frase: ')).upper().strip()
print('\033[31mAnalisando a frase...\033[m')
sleep(1)
print('A letra "A" aparece \033[33m{}\033[m vezes na frase'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição \033[33m{}\033[m'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição \033[33m{}\033[m'.format(frase.rfind('A')+1))
