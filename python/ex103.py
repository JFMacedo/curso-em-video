def ficha(n='<desconhecido>', g=0):
    """
    → Mostra a ficha de um jogador de acordo com os dados informados.
    :param n:
    :param n: Nome do jogador.
    :param g: Números de gols feitos no campeonato.
    :return: Sem retorno.
    """
    print(f'O jogador \033[34m{n}\033[m fez \033[34m{g}\033[m gol(s) no campeonato.')


print(f'\033[33m{" Exercício 103 ":-^51}\033[m')
nome = str(input('Nome do jogador: ')).strip().title()
ng = str(input('Número de gols: '))
if ng.isnumeric():
    ng = int(ng)
else:
    ng = 0
ficha(nome, ng)
