from random import randint
from time import sleep

print("-=-" * 6)
print("   PAR OU IMPAR   ")
print("-=-" * 6)

cont = 0
pi = ''

while True:

    pc = randint(0, 10)
    n = int(input('Digite um número: '))
    total = n + pc

    escolha = input('PAR OU IMPAR? [P/I] ').strip().upper()[0]
    while escolha not in 'PpIi':
        print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
        escolha = input('PAR OU IMPAR? [P/I] ').strip().upper()[0]

    if total % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'IMPAR'

    print(f'Você escolheu {n} e o computador {pc}. Total de {total} e deu {pi}!')

    if escolha == pi[0]:
        cont += 1
        sleep(1)
        print('\033[1;32mVOCÊ GANHOU!!!')
        print('\033[mVamos jogar novamente.')
    else:
        sleep(1)
        print('\033[1;31mVOCÊ PERDEU!!!')
        print(f'\033[mVoce ganhou {cont} vezes!')
        break


'''pi = ''
cont = 0

while True:
    pc = randint(0, 10)
    valor = int(input('Digite um valor: '))
    total = pc + valor
    escolha = input('PAR OU IMPAR? [P/I] ').upper().strip()[0]

    if total % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'IMPAR'

    if escolha != 'P' or escolha != 'I':
        print('OPÇÃO INVALIDA!')
        escolha = input('PAR OU IMPAR? [P/I] ').upper().strip()[0]


    print(f'Você jogou {valor} e a máquina {pc}. Total de {total} deu {pi}! ')

    if escolha == pi[0]:
        sleep(1)
        print('Vitoria')
        print('Vamos jogar novamente!')
        cont += 1
    else:
        sleep(1)
        print('Derrota')
        print(f'Você venceu {cont} vezes!')
        break'''
