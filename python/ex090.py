print(f'\033[33m{" Exercício 090 ":-^51}\033[m')
aluno = {'Nome': str(input('Nome: ')).strip().title(), 'Média': float(input('Média: '))}
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'\033[33m{k}\033[m é igual a \033[32m{v}\033[m')
