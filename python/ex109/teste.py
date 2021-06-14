from ex109 import moeda

print(f'\033[33m{" Exercício 109 ":-^51}\033[m')
p = float(input('\033[35mDigite o peço:\033[32m R$ \033[m'))
print(f'\033[35mA metade de\033[30m {moeda.formato(p)} \033[35mé\033[30m {moeda.metade(p, formato=True)}')
print(f'\033[35mO dobro de\033[30m {moeda.formato(p)} \033[35mé\033[30m {moeda.dobro(p, formato=True)}')
print(f'\033[35mAumentando 10%, temos\033[30m {moeda.aumentar(p, 10, formato=True)}')
print(f'\033[35mDiminuindo 13%, temos\033[30m {moeda.diminuir(p, 13, formato=True)}')
