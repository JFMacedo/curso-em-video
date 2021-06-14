print('\033[7;40;33m{:=^51}\033[m'.format(' Exercício 035 '))
s1 = float(input('Medida do 1º segmento: '))
s2 = float(input('Medida do 2º segmento: '))
s3 = float(input('Medida do 3º segmento: '))
if (s1+s2) > s3 and (s1+s3) > s2 and (s2+s3) > s1:
    print('\033[33mOs segmentos acima formam um triangulo!\033[m')
else:
    print('\033[33mOs segmentos acima não formam um triangulo!\033[m')
