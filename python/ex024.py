print('\033[7;34;40m{:=^51}\033[m'.format(' Exercício 024 '))
cidade = str(input('Digite o nome de uma cidade: ')).upper().strip()
print('\033[34mO nome começa com Santo? {}\033[m'.format(cidade[:5] == 'SANTO'))
