def leiaInt(msg):
    """
    Função criada para verificar se o que foi digitado é um número inteiro.  
    :param msg: valor digitado
    :param valor: verifica se o valor digitado é numérico
    :return: retorna o valor inteiro
    """
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[0;31mERRO!! Digite um número inteiro válido! \033[m')


n = leiaInt('Digite um número: ')
print(f'\033[0;32mVocê acabou de digitar o número {n}\033[m')

'''while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')


n = leiaInt('Digite um número: ')
print(f'\033[0;32mVocê acabou de digitar o número {n}\033[m')'''