matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma3 = maior = spar = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um número para [{l}, {c}]: "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()

print(f"A soma dos valores pares é {spar}.")

for l in range(0, 3):
    soma3 += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {soma3}.")

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}.")

"""for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um número para a posição [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])

        if c == 2:
            soma3 += matriz[l][c]

print('*' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end=' ')
    print()

print('*' *30)

print(f"Os valores pares digitados fora {pares} e sua soma é {sum(pares)}.")
print(f"A soma dos valores da terceira coluna é {soma3}.")
print(f"O maior valor da segunda linha é {max(matriz[1])}.")"""

"""for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f"Digite um valor para {c, l}: "))
        if l == 0:
            matriz[0].append(n)
        elif l == 1:
            matriz[1].append(n)
        elif l == 2:
            matriz[2].append(n)

        if n % 2 == 0:
            pares.append(n)

        if c == 2:
            soma3 += n

print(f"{matriz[0]}", end='')
print(f"\n{matriz[1]}", end='')
print(f"\n{matriz[2]}", end='')

print(f"\nOs valores pares digitados foram {pares} e sua soma foi {sum(pares)}.")
print(f'A soma dos valores da 3ª coluna foram {soma3}.')
print(f"O maior valor da segunda linha é {max(matriz[1])}")"""
