print("-=-"*8)
print("   MAIOR E MENOR PESO!  ")
print("-=-"*8)

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}ª pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
                menor = peso

print(f"A pessoa com maior peso tem {maior}kg.")
print(f"A pessoa com menor peso tem {menor}kg.")


"""
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input("Digite o pedo da {}ª pessoa: ".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print("O maior peso registrado foi {}kg.".format(maior))
print("O menor peso registrado foi {}kg.".format(menor))"""

"""for p in range(1, 6):
    peso = float(input("Digite o peso da 1ª pessoa: ").format(p))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print("O maior peso digitado foi {:.2f} kg".format(maior))
print("O menor peso digitado foi {:.2f} kg".format(menor))"""



