from ex108 import moeda

print(f'\033[33m{" Exercício 108 ":-^51}\033[m')
p = float(input('\033[35mDigite o peço: R$ \033[m'))
print(f'\033[35mA metade de\033[30m {moeda.moeda(p)} \033[35mé\033[30m {moeda.moeda(moeda.metade(p))}')
print(f'\033[35mO dobro de\033[30m {moeda.moeda(p)} \033[35mé\033[30m {moeda.moeda(moeda.dobro(p))}')
print(f'\033[35mAumentando 10%, temos\033[30m {moeda.moeda(moeda.aumentar(p, 10))}')
