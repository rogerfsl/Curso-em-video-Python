def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número inteiro válido. \033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except(ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número inteiro válido. \033[m')
        except(KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digiter um número real: ')
print(f'Valor inteiro digitado {n1} e o real foi {n2}')