temp = []
alunos = []
media = 0

while True:
    nome = input("Nome: ").strip().upper()
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) /2
    alunos.append([nome, [n1, n2], media])

    resp = input("Quer continuar? [S | N] ").strip().upper()
    while resp not in "SsNn":
        resp = input("Quer continuar? [S | N] ").strip().upper()
    if resp == "N":
        break

print(f"{'Nº.':<4}{'Nome':<10}{'Média':>8}")
print('-'*30)
for i, a in enumerate(alunos):
    print(f"{i +1:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print('-' * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe)"))
    if opc == 999:
        print("Finalizando...")
        break
