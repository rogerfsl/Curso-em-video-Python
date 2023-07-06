from random import randint
from time import sleep


def maior(*lst):
    cont = maior = 0
    print('-' * 70)
    print('Esses foram os numeros sorteados: ', end=' ')
    for n in lst:
        print(f'{n}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print()
    print(f'Foram informados {cont} numeros.')
    print(f'O maior número é {maior}.')


maior(randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))
maior(randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))
maior(5, 8, 7, 10)
maior()
