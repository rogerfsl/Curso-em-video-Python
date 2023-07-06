from time import sleep


def clear():
    print('\n' * 50)


def cores(cor, ground):
    background = dict()
    background["Preto"] = "\033[40m"
    background["Vermelho"] = "\033[41m"
    background["Verde"] = "\033[42m"
    background["Amarelo"] = "\033[43m"
    background["Azul"] = "\033[44m"
    background["Magenta"] = "\033[45m"
    background["Ciano"] = "\033[46m"
    background["Branco"] = "\033[47m"
    background["Reset"] = "\033[49m"
    foreground = dict()
    foreground["Preto"] = "\033[30m"
    foreground["Vermelho"] = "\033[31m"
    foreground["Verde"] = "\033[32m"
    foreground["Amarelo"] = "\033[33m"
    foreground["Azul"] = "\033[34m"
    foreground["Magenta"] = "\033[35m"
    foreground["Ciano"] = "\033[36m"
    foreground["Branco"] = "\033[37m"
    foreground["Reset"] = "\033[39m"
    if ground == "background":
        return background[cor]
    if ground == "foreground":
        return foreground[cor]


def titulo(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


def ajuda(com):
    help(com)


# programa principal
comando = ''

while True:
    print(cores("Azul", "background"))
    print(cores("Reset", "foreground"))
    titulo('SISTEMA DE AJUDA PyHELP')
    print(cores("Reset", "background"))
    sleep(1)
    comando = input('Função ou Biblioteca: ').strip()
    if comando.upper() == 'FIM':
        break
    print(cores("Branco", "background"))
    print(cores("Reset", "foreground"))
    sleep(0.5)
    ajuda(comando)
    print(cores("Reset", "background"))

print(cores("Vermelho", "background"))
print(cores("Reset", "foreground"))
print('ATÉ LOGO!!!')
print(cores("Reset", "background"))
