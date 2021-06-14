def area(l, c):
    a = l*c
    print(f'A area de um terreno de {l:.1f}x{c:.1f} é de {a:.1f}m².')


print(f'\033[33m{" Exercício 096 ":-^51}\033[m')
print(f'{"CONTROLE DE TERRENOS":^51}')
print(f'\033[33m-\033[m'*51)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
