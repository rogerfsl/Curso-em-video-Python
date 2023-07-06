from random import randint


def sorteio(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lst.append(randint(1, 10))
        print(f'{lst[c]}', end=' ')


def soma(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'\nSomando os valores pares de {lista}, temos {soma}')


numeros = []
sorteio(numeros)
soma(numeros)