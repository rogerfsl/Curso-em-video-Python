valores = [[], []]

for c in range(1, 8):
    n = int((input(f"digite o {c}º valor: ")))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

print(f"Os números pares digitados foram: {sorted(valores[0])}")
print(f"Os números ímpares digitados foram: {sorted(valores[1])}")


"""for c in range(0, 7):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)

print(f"Esses foram os pares digitados: {sorted(valores[0])}")
print(f"Esses foram os ímpares digitados: {sorted(valores[1])}")"""

"""for p in valores:
    if p % 2 == 0:
        pares.append(p)
    else:
        impar.append(p)"""

"""for p in range(len(valores)):
    if valores[p] %2 == 0:
        pares.append(valores[p])
    else:
        impar.append(valores[p])
"""
