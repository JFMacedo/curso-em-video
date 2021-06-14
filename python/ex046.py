from emoji import emojize
from time import sleep
print('\033[34m{:•^51}\033[m'.format(' Exercício 046 '))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize('\033[31m:fireworks:', use_aliases=True))
