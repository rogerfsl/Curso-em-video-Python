print("-=-" * 6)
print("     FATORIAL    ")
print("-=-" * 6)

n = int(input("Digite o o número que deseja saber o fatorial: "))
c = n
f = 1

print(f'Fatorial de {n}! = ', end=" ")
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=" ")
    f *= c
    c -= 1

print(f)

"""n = int(input('Fatorial de: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1

print(f'{f}')"""

"""num = int(input("Fafotial de: "))

cont = 1
fat = 1

while cont <= num:
    fat *= cont
    cont += 1

print(f"{num}! = {fat}")"""

"""num = int(input("Digite um número: "))
cont = 1
fat = 1

while cont <= num:
    fat = fat * cont
    cont += 1

print(f'{num}! = {fat}')"""

"""num = int(input("Fatorial de: "))
fat = 1
cont = 1

while cont <= num:
    fat *= cont
    cont += 1


print(f'{num}! = {fat}')"""

"""for c in range(num, 0, -1):
    fat *= c

print(f'{num}! = {fat}')"""

"""n = int(input("Fatorial de: "))
r = 1

for c in range(1, n + 1):
    r *= c
print(f'\n{n}! = {r}')"""


