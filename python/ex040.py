print('\033[30m{:=^51}\033[m'.format(' Exercício 040 '))
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2
print('Com as notas \033[30m{:.1f}\033[m e \033[30m{:.1f}\033[m, a média do aluno é \033[30m{:.1f}\033[m'.format(n1, n2, media))
if media < 5:
    print('Aluno \033[31mREPROVADO!\033[m')
elif media >= 5 and media < 7:
    print('Aluno em \033[33mRECUPERAÇÃO!\033[m')
elif media >= 7:
    print('Aluno \033[32mAPROVADO!\033[m')
