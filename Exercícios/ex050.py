print("-=-"*8)
print("     SOMA DOS PARES!     ")
print("-=-"*8)

spar = 0
contp = 0
for c in range(1, 7):
    n = int(input("Digite o {}° valor: ".format(c)))
    if n % 2 == 0:
        spar += n
        contp += 1

print("Foram digitados {} numeros pares e soma deles é {}.".format(contp, spar))

"""s = 0
cont = 0
si = 0
cont2 = 0
for c in range(1, 7):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        s += n
        cont += 1
    else:
        n % 2 == 1
        si += n
        cont2 += 1
print("Você informou {} valores pares e a soma deles é {}!".format(cont, s))
print("Você digitou {} numeros ímpares e a soma deles é {}!".format(cont2, si))"""

