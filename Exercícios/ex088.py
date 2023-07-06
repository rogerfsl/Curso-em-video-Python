from random import randint
from time import sleep

lista = []
jogo = []

quant = int(input("Quantos jogos deseja fazer? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    tot += 1

for i, c in enumerate(jogo):
    print(f"Jogo {i +1}: {c}")
    sleep(1)


"""sorteio = []
cont = 0

jogos = int(input("Quantos jogos deseja criar? "))

print(f"Sorteando {jogos} jogos!")
while jogos not in range(0, jogos):

    for c in range(0, 6):
        n = randint(1, 60)
        if n not in sorteio:
            sorteio.append(n)
        else:
            n = randint(1, 60)
            sorteio.append(n)

    print(f"Jogo {cont + 1}: {sorted(sorteio)}")
    sleep(1)
    cont += 1
    sorteio.clear()
    if cont == jogos:
        break"""

"""for c in range(0, 6):
        n = randint(1, 60)
        provisorio.append(n)
        if n in provisorio:
            provisorio.remove(n)
            provisorio.append(randint(1, 60))
    sorteio.append(provisorio[:])
    provisorio.clear()"""

