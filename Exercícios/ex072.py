contagem = 'zero', 'um', 'dois', 'três', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', \
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    n = int(input("Digite um número entre 0 e 20: "))

    while n not in range(0, 21):
        n = int(input("Número inválido! Digite um número entre 0 e 20: "))

    print(f"Você digitou o número {contagem[n]}")
    resp = input("Deseja continuar? [S | N] ").strip().upper()

    while resp not in "SN":
        resp = input("Deseja continuar? [S | N] ").strip().upper()

    if resp == "N":
        break
print("Programa finalizado!")


"""while True:
    
    n = int(input("Digite um número entre 0 e 20: "))

    if 0 <= n <= 20:
        break
    print("Tente novamente.", end=" ")
print(f"Você digitou o número {contagem[n]}")"""

"""while True:

    n = int(input("Digite um número entre 0 e 20: "))

    while n not in range(0, 21):
        n = int(input("Opção inválida! Digite um número entre 0 e 20: "))

    print(f"Você digitou o número {contagem[n]}")

    resp = input("Deseja continuar? [S | N] ").strip().upper()

    while resp not in "SN":
        resp = input("Deseja continuar? [S | N] ").strip().upper()

    if resp == "N":
        print("Programa finalizado!")
        break"""

"""while True:

    perg = int(input('Digite um número entre 0 e 20: '))

    while perg not in range(0, 21):
        perg = int(input('Tentativa Inválida! Digite um número entre 0 e 20: '))

    print(f'Você digitou o número {contagem[perg]}')
    resp = input("Quer continuar? [S | N] ").strip().upper()

    while resp not in "SN":
        resp = input("Quer continuar? [S | N] ").strip().upper()

    if resp == 'N':
        print("Programa finalizado!")
        break"""

'''while resp not in 'Nn':
    perg = int(input("Digite um número entre 0 e 20: "))

    while perg not in range(0, 21):
        perg = int(input("Tente novamente! Digite um número entre 0 e 20: "))

    print(f'Você digitou o número {contagem[perg]}')
    resp = input('Quer continuar? [S/N] ').strip().upper()'''
