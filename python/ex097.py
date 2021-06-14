def escreva(msg):
    print('\033[35m~\033[m'*(len(msg)+2))
    print(f' {msg} ')
    print('\033[35m~\033[m'*(len(msg)+2))


print(f'\033[33m{" Exercício 097 ":-^51}\033[m')
escreva('Jean Feranandes de Macedo')
escreva('Python')
escreva('Jéssica Laís Cuaglio')
