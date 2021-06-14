print('\033[30;43m{:=^51}\033[m'.format(' Exercício 025 '))
nome = str(input('Digite um nome: ')).lower().strip()
print('\033[033mTem Silva no nome: {}\033[m'.format('silva' in nome))
