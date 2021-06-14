def voto(ano):
    """
    → Analisa o ano de nacimento de uma pessoa e retorna a situação de voto.
    :param ano: ano de nascimento da pessoa.
    :return: situação de voto.
    Função criada por Jean Fernandes de Macedo
    """
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    if 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


print(f'\033[33m{" Exercício 101 ":-^51}\033[m')
ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
