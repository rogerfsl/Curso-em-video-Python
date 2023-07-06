print("-=-"*8)
print("     É UM PALINDROMO?   ")
print("-=-"*8)

frase = input("Digite uma frase: ").strip().upper()
pa = frase.replace(" ", "")
inverso = pa[::-1]

print("O inverso de {} é {}.".format(pa, inverso))
if pa == inverso:
    print("\033[32mEssa frase é um palíndromo!")
else:
    print("\033[31mEssa frase não é um palindromo!")

"""frase = input("Digite uma frase: ").strip().upper()
palavra = frase.split()
td = ''.join(palavra)
inverso = ''
for letra in range(len(td) -1, -1, -1):
    inverso += td[letra]
print("O inverso de {} é {}.".format(td, inverso))
if inverso == td:
    print("Temos um palíndromo!")
else:
    print("Não temos um palíndromo")"""

"""frase = str(input("Digite uma frase: ")).strip().upper()
pa = frase.replace(" ", '')
inverso = pa[::-1]

print("A frase {}".format(pa), end=" ")
print("invertida fica {}".format(inverso))

if inverso == pa:
    print("A frase é um palindromo!")
else:
    print("A frase não é um palimdromo!")"""

"""frase = str(input("Digite uma frase: ")).strip().upper()
pa = frase.replace(" ", "")
inverso = pa[::-1]

print("Você digitou a frase: {}".format(pa))
print("Seu inverso é: {}".format(inverso))

if inverso == pa:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo!")"""






