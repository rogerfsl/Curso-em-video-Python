def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mERRO!!! OPERAÇÃO INVÁLIDA\033[m')
        else:
            return float(entrada)


def leiaInt(msg):
    """
    Função criada para verificar se o que foi digitado é um número inteiro.
    :param msg: valor digitado
    :param valor: verifica se o valor digitado é numérico
    :return: retorna o valor inteiro
    """
    while True:
        valor = input(msg).strip().replace(',', '.')
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[0;31mERRO!! Digite um número inteiro válido! \033[m')