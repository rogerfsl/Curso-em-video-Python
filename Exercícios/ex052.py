print("-=-" * 8)
print("    O NÚMERO É PRIMO?   ")
print("-=-" * 8)

n = int(input("Digite um número: "))
cont = 0

for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print("\033[32m", end=' ')
    else:
        print("\033[31m", end=' ')
    print("{}".format(c), end=" ")
print("\n\033[mO número {} foi divisível {} vezes!".format(n, cont))

if cont == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele não é primo!")

"""n = int(input("Digite um número: "))
cont = 0

for c in range(1, n +1):
    if n % c == 0:
        cont += 1
        print("\033[32m", end=' ')
    else:
        print("\033[31m", end=' ')
    print("{}".format(c), end=' ')
print("\n\033[mO número {} foi divisível {} vezes!".format(n, cont))

if cont == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele não é primo!")"""

"""n = int(input("Digite um número: "))
cont = 0

for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print("\033[32m", end=" ")
    else:
        print("\033[31m", end=' ')
    print("{}".format(c), end=' ')
print("\n\033[mO número {} foi divisível {} vezes.".format(n, cont))

if cont == 2:
    print("É PRIMO")
else:
    print("NÃO É PRIMO")"""

"""n = int(input("Digite um número: "))
cont = 0

for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
print("O número {} foi divisivel {} vezes".format(n, cont))

if cont == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele não primo!")"""

"""n = int(input("Digite um número: "))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[32m", end=" ")
        cont += 1
    else:
        print("\33[31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[mO número {} foi divisível {} vezes.".format(n, cont))
if cont == 2:
    print("E por isso o número {} é primo!".format(n))
else:
    print("E por isso o número {} não é primo!".format(n))"""
