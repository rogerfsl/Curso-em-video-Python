def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite uma opção válida, \033[m')
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lst):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lst:
        print(f'\033[34m{c} - {item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção: \033[m')
    return opc
