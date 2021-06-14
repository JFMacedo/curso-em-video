print(f'\033[32m{" Exercício 083 ":-^51}')
exp = str(input('Digite uma expressão: '))
cont1 = cont2 = 0
for i in range(0, len(exp)):
    if i == '(':
        cont1 += 1
    elif i == ')':
        cont2 +=1
if cont1 == cont2:
    print('Sua expressão está correta')
else:
    print('Sua expressão está errada')
