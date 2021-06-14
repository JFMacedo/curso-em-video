def notas(*nota, sit=False):
    """
    → Função para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais notas dos alunos (aceita várias).
    :param sit: (opcional) Indica se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dic = {}
    dic['Total'] = len(nota)
    dic['Maior'] = max(nota)
    dic['Menor'] = min(nota)
    dic['Média'] = sum(nota)/len(nota)
    if sit:
        if dic['Média'] < 5:
            dic['Situação'] = 'RUIM'
        elif dic['Média'] >= 7:
            dic['Situação'] = 'BOA'
        else:
            dic['Situação'] = 'RAZOÁVEL'
    return dic


resp = notas(5.5, 5, 8, 6.5, 10, sit=True)
print(resp)
