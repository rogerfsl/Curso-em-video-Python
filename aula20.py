def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)

'''def dobra(lst):
    pos = 0
    while pos <(len(lst)):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)
print(valores)
'''

"""from random import randint


def contador(* num):
    tam = len(num)
    print(f'Recebi os valore {num} e ao todo são {tam}!')


contador(randint(0, 10), randint(0, 10), randint(0, 10))
contador(randint(0, 10), randint(0, 10))
contador(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))"""

"""def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre {a} e {b} é igual a {s}')


soma(b=4, a=5)
print()
soma(7, 2)"""

"""def titulo(txt):
    print('-' * 20)
    print(txt)
    print('-' * 20)


# programa principal
titulo('   Curso em Vídeo!  ')"""
