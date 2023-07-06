matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valo para [{l},{c}]: "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l] [c]:^3}]", end='')
    print()

"""for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f"Digite um número para {c, l} "))
        if l == 0:
            matriz[0].append(n)
        if l == 1:
            matriz[1].append(n)
        if l == 2:
            matriz[2].append(n)

print(f"{matriz[0]}", end='')
print(f"\n{matriz[1]}", end='')
print(f"\n{matriz[2]}", end='')"""
