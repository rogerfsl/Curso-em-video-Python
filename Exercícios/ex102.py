print("-=-" * 6)
print("     FATORIAL    ")
print("-=-" * 6)


def fatorial(num, show=False):
    """
    :param num: Número a ser calculado
    :param show: (opcional) Mostra ou nao a conta.
    :return: O valor do fatorial de um número (num)
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f

while True:
    n = int(input('Fatorial de: '))
    caminho = input('Deseja ver o caminho? [S | N] ').strip().upper()[0]
    if caminho == 'S':
        print('-=-' * 30)
        print(fatorial(n, True))
    else:
        print('-=-' * 30)
        print(fatorial(n))

    resp = input('Deseja continuar? [S | N] ').strip().upper()[0]
    while resp not in 'SsNn':
        resp = input('Deseja continuar? [S | N] ').strip().upper()[0]
    if resp == 'N':
        print('VOLTE SEMPRE!')
        break
# help(fatorial)
