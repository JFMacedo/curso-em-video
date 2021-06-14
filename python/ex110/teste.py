from ex110 import moeda

print(f'\033[33m{" Exercício 109 ":-^51}\033[m')
p = float(input('\033[30mDigite o peço:\033[32m R$ \033[m'))
moeda.resumo(p, 20, 12)
