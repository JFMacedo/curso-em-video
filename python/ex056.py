print('\033[7;36;40m{:•^51}\033[m'.format(' Exercício 056 '))
soma = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1, 5):
    print('\n{:-^51}'.format(' \033[33m{}ª Pessoa\033[m '.format(pessoa)))
    nome = str(input('\033[36mNome\033[m: ')).strip().upper()
    idade = int(input('\033[36mIdade\033[m: '))
    sexo = str(input('\033[36mSexo [M/F]\033[m: ')).strip().upper()
    soma = soma+idade
    if pessoa == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        totmulher20 = totmulher20+1
print('\n\033[35mA média de idade do grupo é \033[33m{:.0f} anos\033[m.'.format(soma / 4))
print('\033[35mO homem mais velho tem \033[33m{}\033[35m anos e se chama \033[33m{}\033[m.'.format(maioridadehomem, nomevelho))
print('\033[35mAo total são \033[33m{} mulheres\033[35m com menos de 20 anos\033[m.'.format(totmulher20))