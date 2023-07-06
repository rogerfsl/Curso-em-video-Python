from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    resp = menu(['Cadastrar nova pessoa', 'Ver pessoas cadastradas', 'Sair do Sistema'])
    if resp == 1:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastro(arq, nome, idade)
    elif resp == 2:
        # opção de listar o conteúdo de um arquivo.
        lerarquivo(arq)
    elif resp == 3:
        cabeçalho('Encerrando...')
        sleep(0.5)
        break
    else:
        print('\033[0:31mERRO!!! Digite uma opção válida.\033[m')
        sleep(1)
