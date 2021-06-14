print(f'\033[35m{" Exercício 085 ":-^51}\033[m')
lista = [[], []]
for c in range(1, 8):
       num = int(input(f'Digite o {c}º valor: '))
       if num % 2 == 0:
             lista[0].append(num)
       else:
             lista[1].append(num)
print('\033[35m-\033[m'*51)
if len(lista[0]) == 0:
       print('\033[31mNenhum valor par foi digitado!\033[m')
else:
    print(f'Os Valores pares digitados foram: \033[36m{sorted(lista[0])}\033[m')
if len(lista[1]) == 0:
       print('\033[31mNenhum valor ímpar foi digitado!\033[m')
else:
    print(f'Os Valores ímpares digitados foram: \033[36m{sorted(lista[1])}\033[m')
