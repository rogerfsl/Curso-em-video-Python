valores = []

for v in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {v}: ")))

print(f"Você digitou os valores {valores}")
print(f"Os valores digitados em ordem crescente {sorted(valores)}")

print(f"O maior valor digitado foi {max(valores)} e está nas posições ", end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f"{c}", end='')

print(f"\nO menor valor digitado foi {min(valores)} e está nas posições ", end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f"{c}", end='')
print("\nPrograma finalizado!")

"""for v in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {v}: ")))

print(f"Você digitou os valores: {valores}")
print(f"Os valores digitados em ordem crescente ficam: {sorted(valores)}")
print(f"O maior número digitado foi {max(valores)} e ele está na posição ", end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f"{c}", end=' ')

print(f"\nO menor valor digitado foi {min(valores)} e ele está na posição ", end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f"{c}", end=' ')

print("\nFim do Programa!")"""

"""for n in range(0, 5):
    valores.append(int(input(f"Digite um número inteiro na posição {n + 1}: ")))

print(f"Os valores digitados foram {valores}")
print(f"Os valores digitados em ordem são {sorted(valores)}")
valores.sort(reverse=True)
print(f"Os valores digitados em ordem inversa são {valores}")

print(f"O maior valor digitado foi {max(valores)} nas posições ", end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f"{c + 1} ", end='')

print(f"\nO menor valor digitado foi {min(valores)} nas posições ", end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f"{c + 1} ", end='')

print("\nPrograma finalizado!!!")"""

"""for n in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {n + 1}: ")))

print(f"Os valores digitados foram {valores}")

print(f"O maior valor digitado foi {max(valores)} nas posições  ", end='')
for c, v in enumerate(valores):
    if v == max(valores):
        print(f"{c + 1} ", end='')

print(f"\nO menor valor digitado foi {min(valores)} nas posições ", end='')
for c, v in enumerate(valores):
    if v == min(valores):
        print(f"{c + 1} ", end='')"""

"""for n in range(0, 5):
    valores.append(int(input(f"Digite um número inteiro para a posição {n + 1}: ")))

print(f"Os valores digitados foram {valores}")

print(f"O maior valor digitado foi {max(valores)} na posição ", end='')

for c, v in enumerate(valores):
    if max(valores) == v:
        print(f"{c +1}...", end="")

print(f"\nO menor valor digitado foi {min(valores)} na posição ", end='')

for c, v in enumerate(valores):
    if v == min(valores):
        print(f"{c + 1}...", end='')

print("\nPROGRAMA FINALIZADO!")"""

