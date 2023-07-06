valores = []

while True:
    n = int(input("Digite um número inteiro: "))

    valores.append(n)

    resp = input("Quer continuar [S | N] ").strip().upper()
    while resp not in "SN":
        resp = input("Quer continuar [S | N] ").strip().upper()

    if resp == "N":
        print("Programa Finalizado!")
        break

print(f"Voce digitou {len(valores)} números na lista ")
valores.sort(reverse=True)
print(f"Os valores digitados em ordem decrescente são: {valores} ")

if 5 in valores:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista!")
