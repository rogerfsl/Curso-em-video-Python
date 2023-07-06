from random import randint
from time import sleep

numero_secreto = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar!")
print("-=-" * 20)
chute = int(input("Digite o seu chute: "))
print("PROCESSANDO...")
sleep(2)
if chute == numero_secreto:
    print("ACERTOU MIZERAVI!!!")
else:
    print("ERROU!!!")
print("O seu chute foi {} e o número secreto é {}".format(chute, numero_secreto))



# meu código.
# numero_secreto = rd.randrange(0, 6)
# chute = int(input("Digite um número de 0 até 5: "))

# if chute == numero_secreto:
    # print("Acertou mizeravi!")
# else:
    # print("ERROU!!!")
# print("O número secreto é {} ".format(numero_secreto))

