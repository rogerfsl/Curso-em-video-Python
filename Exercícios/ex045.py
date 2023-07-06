from random import randint

print("PEDRA, PAPEL E TESOURA!")

print(""" OPÇÕES: 
[1] PEDRA
[2] PAPEL
[3] TESOURA""")

opção = int(input("Escolha uma opção: "))
maquina = randint(1, 3)

if opção == 1 and maquina == 1:
    print("Você escolheu PEDRA E máquina escolheu PEDRA.")
    print("Empate")
elif opção == 1 and maquina == 2:
    print("Você escolheu PEDRA e a máquina escolheu PAPEL.")
    print("Máquina ganhou!")
elif opção == 1 and maquina == 3:
    print("Você escolheu PEDRA e a máquina escolheu TESOURA.")
    print("Jogador venceu!")
elif opção == 2 and maquina == 1:
    print("Você escolheu PAPEL e a máquina PEDRA.")
    print("Jogador ganhou!")
elif opção == 2 and maquina == 2:
    print("Você escolheu PAPEL e a máquina PAPEL")
    print("Empate!")
elif opção == 2 and maquina == 3:
    print("Você escolheu PAPEL e a máquina TESOURA")
    print("Máquina venceu!")
elif opção == 3 and maquina == 1:
    print("Você escolheu TESOURA e a máquina PEDRA")
    print("Máquina venceu!")
elif opção == 3 and maquina == 2:
    print("Você escolheu TESOURA e a máquina PAPEL")
    print("Jogador venceu!")
elif opção == 3 and maquina == 3:
    print("Você escolheu TESOURA e a máquina TESOURA")
    print("Empate!")
