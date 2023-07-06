

print("\033[4;34; m---PODE FORMAR UM TRIÂNGULO?---\033[m")

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\033[1;35; mÉ possível criar um triângulo!\33[m")
else:
    print("\033[1;31; mNão é possivel criar um triângulo\33[m")
