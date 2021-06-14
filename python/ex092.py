from datetime import date
print(f'\033[33m{" Exercício 092 ":-^51}\033[m')
dados = {}
dados['Nome'] = str(input('Nome: ')).strip().title()
Nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year-Nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] > 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Contratação']+35-dados['Nascimento']
print('\033[33m-\033[m'*51)
for k, v in dados.items():
    print(f'\033[34m{k}\033[m tem o valor \033[32m{v}\033[m')
