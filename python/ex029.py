print('\033[7;31m{:=^51}\033[m'.format(' Exercício 029 '))
v = int(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80K/h\nVocê deve pagar uma multa de '
          '\033[1mR$ {:.2f}\033[m'.format((v-80)*7))
print('\033[34mTenha um bom dia! Dirija com segurança!\033[m')
