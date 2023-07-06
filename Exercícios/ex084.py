pessoas = []
status = []
maior = menor = 0

while True:
    status.append(input("Nome: ").strip().upper())
    status.append(int(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = status[1]
    else:
        if status[1] > maior:
            maior = status[1]
        elif status[1] < menor:
            menor = status[1]

    pessoas.append(status[:])
    status.clear()

    resp = input("Quer continuar? [S | N] ").strip().upper()
    if resp == "N":
        break

print(f"Foram cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso registrado foi {maior}")
print(f"O menor peso registrado foi {menor}")
"""maior = menor = 0

while True:
    status.append(input("Nome: ").strip().upper())
    status.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = status[1]
    else:
        if status[1] > maior:
            maior = status[1]
        elif status[1]< menor:
            menor = status[1]

    pessoas.append(status[:])
    status.clear()

    resp = input("Quer continuar? [S | N] ").strip().upper()
    if resp == "N":
        break

print(f"Ao todo foram cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso registrado foi de {maior}kg, e foi de: ", end='')
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')

print(f"\nO menor peso registrado doi de {menor}kg, e foi de: ", end='')
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')"""

"""maior = menor = 0

while True:
    status.append(input("Nome: ").strip().upper())
    status.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = status[1]
    else:
        if status[1] > maior:
            maior = status[1]
        elif status[1] < menor:
            menor = status[1]

    pessoas.append(status[:])
    status.clear()

    resp = input("Quer continuar? [S | N] ").strip().upper()
    if resp == "N":
        break

print(maior)
print(menor)

print(f"Ao todo foram cadastradas {len(pessoas)} pessoas.")
print(f"O maior peso registrado foi de {maior}kg, e foi de: ", end='')
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=" ")
print(f"\nO menor peso registrado foi de {menor}, e foi de: ", end='')
for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]}", end=' ')"""

"""maior = menor = 0

while True:
    status.append(input("Nome: ").strip().upper())
    status.append(float(input("Peso: ")))

    if len(pessoas) == 0:
        maior = menor = status[1]
    else:
        if status[1] > maior:
            maior = status[1]
        elif status[1] < menor:
            menor = status[1]

    pessoas.append(status[:])
    status.clear()
    resp = input("Quer continuar [S | N] ").strip().upper()
    if resp == "N":
        print("Programa finalizado!")
        break

print(f"Foram cadastradas {len(pessoas)} pessoas!")
print(f"O maior peso registrado foi de {maior}, e foi de: ", end='')
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')

print(f"\nO menor peso registrado foi de {menor}, e foi de: ", end='')
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')
"""

"""maior = menor = 0

while True:
    status.append(input("Nome: "))
    status.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = status[1]
    else:
        if status[1] > maior:
            maior = status[1]
        elif status[1] < menor:
            menor = status[1]

    pessoas.append(status[:])
    status.clear()

    resp = input("Quer continuar? [S | N] ").strip().upper()
    while resp not in "SsNn":
        resp = input("Quer continuar? [S | N] ").strip().upper()

    if resp in "N":
        print("Programa finalizado!")
        break

cont = 0
for p in pessoas:
    cont += 1
print(f"Foram cadastradas {cont} pessoas!")
print(f"O maior peso registrado foi de {maior}, e foi de: ", end='')
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')
print(f"\nO menor peso cadastrado foi de {menor}, e foi de: ", end='')
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')"""


