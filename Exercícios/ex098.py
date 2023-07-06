from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=-' * 30)
    print(f'Fazendo contagem de {i} até {f} de {p} em {p}!')
    sleep(1)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('FIM!!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=-' * 30)
print('Agora escolha os valores: ')
n1 = int(input("Início: "))
n2 = int(input("Fim:    "))
pas = int(input('Passo: '))
contador(n1, n2, pas)

"""
def contador(n1, n2, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-=-' * 25)
    print(f'Contagem de {n1} até {n2} de {p} em {p}')
   # sleep(1)
    cont = n1
    if n1 < n2:
        cont = n1
        while cont <= n2:
            print(f'{cont}', end=' ')
           # sleep(0.5)
            cont += p
    else:
        cont = n1
        while cont >= n2:
            print(f'{cont}', end=' ')
           # sleep(0.5)
            cont -= p
    print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=-' * 25)
i = int(input('Início: '))
f = int(input('Fim:    '))
pas = int(input('Passo:   '))
contador(i, f, pas)
"""
