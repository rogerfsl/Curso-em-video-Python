valores = []
valores_pares = []
valores_impar = []

while True:
    n = int(input("Digite um número inteiro: "))

    valores.append(n)

    resp = input("Quer continuar? [S | N] ").strip().upper()
    if resp == "N":
        print("Programa finalizado!")
        break

for c in range(len(valores)):
    if valores[c] % 2 == 0:
        valores_pares.append(valores[c])
    else:
        valores_impar.append(valores[c])

print(f"Você digitou os valores: {valores}")
print(f"Esses são os valores pares digitados: {valores_pares}")
print(f"Esses são os valores ímpares digitados: {valores_impar}")