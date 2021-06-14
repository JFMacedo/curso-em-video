def fatorial(num, show=False):
    """
    → Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcinal) Mostrar ou não a conta.
    :return: O valor fatorial do número num.
    """
    tot = 1
    for c in range(num, 0, -1):
        tot *= c
        if show:
            if c == 1:
                print(f'{c}', end=' = ')
            else:
                print(f'{c}', end=' x ')
    return tot


print(f'\033[33m{" Exercício 102 ":-^51}\033[m')
print(fatorial(7, True))
