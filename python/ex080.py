print(f'\033[35m{" Exercício 080 ":-^51}\033[m')
lista = []
for c in range(0, 5):
    num = int(input('\033[36mDigite um valor\033[m: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição \033[33m{pos}\033[m da lista...')
                break
            pos = pos+1
print('\033[35m-\033[m'*51)
print(f'\033[36mOs valores digitados foram\033[m: {lista}.')