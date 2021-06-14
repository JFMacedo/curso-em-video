from math import sin, cos, tan, radians
print('{:=^51}'.format(' Exercício 018 '))
a = float(input('Digite um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('\033[7;34;40mO valor do seno é: {:.4}\033[m\n\033[7;30;41mO valor do cosseno é: {:.4}\033[m\n'
      '\033[7;31;40mO valor da tangente é: {:.4}\033[m'.format(s, c, t))
