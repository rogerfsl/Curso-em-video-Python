def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


escreva('CURSO EM VÍDEO')
escreva('CURSO DE PYTHON NO YOUTUBE')
escreva('CSV')
frase = input('Digite uma frase: ')
escreva(frase)
