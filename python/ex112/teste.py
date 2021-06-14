from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

print(f'\033[33m{" Exercício 109 ":-^51}\033[m')
p = dado.leiadinheiro('\033[30mDigite o preço:\033[32m R$ \033[m')
moeda.resumo(p, 35, 22)
