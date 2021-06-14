print('{:=^51}'.format(' Exercício 011 '))
l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da perece? '))
m = l*a
print('\033[36mA area da parede é {:.2f}m²\033[m\n\033[35mSerá necessário {:.2f}L de tinta para pinta-la!\033[m'.format(m, m/2))
