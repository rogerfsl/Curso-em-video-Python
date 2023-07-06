n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o último valor: '))
tup = (n1, n2, n3, n4)

print("Os numeros digitados foram: ", end='')

for c in tup:
    print(c, end=' ')

print(f"\nO número 9 foi digitado {tup.count(9)} vezes. ")

if 3 in tup:
    print(f"O número 3 foi digitado na posição {tup.index(3)+1}ª.")
else:
    print("O número 3 não foi digitado nenhuma vez.")

print('Os valores pares digitados foram ', end='')
for n in tup:
    if n % 2 == 0:
        print(n, end=' ')

"""print(f'O valor 9 foi digitado {tup.count(9)} vezes.')
if 3 in tup:
    print(f'O valor primeiro valor 3 foi digitado na posição {tup.index(3)+1}')
else:
    print('O numero 3 foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for n in tup:
    if n % 2 == 0:
        print(n, end=' ')"""


