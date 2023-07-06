from random import randint

numero_secreto = randint(0, 10)
certo = False
cont = 0

while not certo:
    cont += 1
    chute = int(input("Digite um número entre 0 e 10: "))

    if chute == numero_secreto:
        certo = True
        print("PARABÉNS!! VOCÊ ACERTOU!")
        print(f'Você precisou de {cont} tentativas para adivinhar o número secreto!')
    else:

        if chute > 10:
            print("Número fora dos parâmetros!")
            print('Volte e digite um número entre 0 e 10.')
        else:

            if chute > numero_secreto:
                print("Você errou!")
                print('O número digitado é maior que o número secreto!')
            elif chute < numero_secreto:
                print('Você errou!')
                print('O número digitado é menor que o número secreto!')

print("Fim de Jogo!")

"""from random import randint
from time import sleep

numero_secreto = randint(0, 10)
c = 0
certo = False

print("-=-" * 10)
print("     Jogo da adivinhação!    ")
print("-=-" * 10)

while not certo:
    c += 1
    chute = int(input("Digite um número de 0 até 10: "))
    if chute == numero_secreto:
        certo = True
        sleep(0.5)
        print("ACERTOU MIZERAVI!!")
        sleep(0.5)
        print(f"Você Precisou de {c} tentativas para finalizar o jogo!")
        break
    else:
        if chute > 10:
            sleep(0.5)
            print("Número digitado não está nos parâmetros!")
            sleep(0.5)
            print("Volte e digite um número de 0 até 10")
        elif chute < numero_secreto:
            print("Você errou!")
            sleep(0.5)
            print("O número digitado é menor que o número secreto!")
        else:
            print("Você errou!")
            sleep(0.5)
            print("O numero digitado é maior que o número secreto!")

print("Fim de jogo!")"""


