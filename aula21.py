def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))
if par(num):
    print("É par!")
else:
    print("É impar!")


"""def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
       # print(f'{f}', end=' ')
    return f


n = int(input("Fatorial de: "))
print(f'fatorial de {n} é: {fatorial(n)}')"""

"""def somar (a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(2, 8)

print(f'As somas são {r1}, {r2}, {r3}')"""

"""def teste():
    x = 8
    print(f'Na função teste. n vale {n}')
    print(f'Na função teste, x vale {x}')

# programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print()
print(f'No programa principal, x vale {x}')"""

'''def somar(a=0, b=0, c=0): 
    """
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :param s: variável para soma
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar(c=3, a=2)
somar()'''

'''def contador(i, f, p):
    """
    -> faz uma contagem de um número até outro e mostra na tela.
    O número inicial não pode ser maior que o final.
    :param i: inicio da contagem
    :param f: fim
    :param p: passo
    :return: sem retorno 
    :param c: contador
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


contador(2, 10, 2)
help(contador)'''