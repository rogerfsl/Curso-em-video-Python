from time import sleep

print("-=-" * 10)
print("     OPERAÇÕES MATEMÁTICAS!    ")
print("-=-" * 10)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
opção = 0
p = ''

while opção != 5:
    print("""OPÇÕES:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA""")

    opção = int(input("Digite a opção desejada: "))

    if opção == 1:
        print(f"A soma entre {n1} e {n2} é igual a {n1 + n2}")

    elif opção == 2:
        print(f"A multiplicação entre {n1} e {n2} é igual a {n1 * n2}")

    elif opção == 3:

        if n1 > n2:
            print(f'Entre {n1} e {n2}.')
            print(f"O maior valor é {n1}.")
        else:
            print(f'Entre {n1} e {n2}.')
            print(f"O maior valor é {n2}.")

    elif opção == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

    elif opção == 5:
        p = input("Tem certeza? [S/N] ").upper()

        if p == 'S':
            sleep(1)
            print("Fim da operação!")
            break
        else:
            print("Voltando para as opções!")
            sleep(1)
    else:
        print("Opção Inválida!")
        sleep(0.5)
        print("Tente novamente!")
    print("-=-" * 10)
    sleep(2)
print("Fim do programa! Volte sempre!!!")
