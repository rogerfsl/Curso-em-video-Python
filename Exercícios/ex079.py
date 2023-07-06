valores = []

while True:
    n = int(input("Digite um número: "))

    if n not in valores:
        print('Valor adicionado!')
        valores.append(n)
    else:
        print("Valor duplicado não pode ser adicionado!")


    resp = input("Quer continuar? [S | N] ").strip().upper()
    while resp not in "SN":
        resp = input("Quer continuar? [S | N] ").strip().upper()

    if resp == 'N':
        print("Programa Finalizado!")
        break

print(f"Você digitou os valores {sorted(valores)}")

"""while True:

    n = int(input("Digite um número: "))

    if n not in valores:
        print("Valor adicionado!")
    else:
        print("Valor duplicado não pode ser adicionado!")
        valores.remove(n)

    valores.append(n)

    resp = input("Deseja continuar? [S | N] ").strip().upper()
    if resp == 'N':
        print(f"Os valores digitados foram {sorted(valores)}")
        break
print("Programa finalizado!")"""
