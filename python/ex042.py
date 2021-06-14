print('\033[36m{:=^51}\033[m'.format(' Exercício 042 '))
s1 = float(input('\033[30mPrimeiro segmento: \033[m'))
s2 = float(input('\033[30mSegundo segmento: \033[m'))
s3 = float(input('\033[30mTerceiro segmento: \033[m'))
if (s1+s2) > s3 and (s2+s3) > s1 and (s3+s1) > s2:
    if s1 == s2 == s3:
        print('\033[36mOs segmentos PODEM formar um triângulo Equilátero.\033[m')
    elif s1 == s2 and s1 != s3 or s1 != s2 and s1 == s3 or s2 == s1 and s2 != s3:
        print('\033[36mOs segmentos PODEM formar um triângulo Isoceles.\033[m')
else:
    print('\033[36mOs segmentos NÃO PODEM formar um triângulo.\033[m')
