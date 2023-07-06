print("QUAL É O TIPO DE TRIÂNGULO?")

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos digitados podem formar um triângulo.")
    if r1 == r2 and r2 == r3:
        print("E formam um triângulo EQUILÁTERO.")
    elif r1 != r2 and r1 != r3 and r3 != r1:
        print("E formam um triângulo ESCALENO.")
    else:
        print("E formam um triângulo ISÓSCELES.")

else:
    print("Os segmentos digitados nao podem formar um triângulo.")
