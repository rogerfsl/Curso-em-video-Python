from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
maquina = randint(0, 2)

print("PEDRA, PAPEL E TESOURA!")
print(""" OPÇÕES: 
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

jogador = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

print("="*28)
print("O jogador escolheu {}!".format(itens[jogador]))
print("A Máquina escolheu {}!".format(itens[maquina]))
print("="*28)

if maquina == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCEU!")
    elif jogador == 2:
        print("MÁQUINA VENCEU!")
    else:
        print("JOGADA INVÁLIDA!")
elif maquina == 1:
    if jogador == 0:
        print("MÁQUINA VENCEU!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCEU!")
    else:
        print("JOGADA INVÁLIDA!")
elif maquina== 3:
    if jogador == 0:
        print("JOGADOR VENCEU!")
    elif jogador == 1:
        print("MÁQUINA VENCEU!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA!")

