n = cont = soma = 0

while n != 999:
    n = int(input("Digite um número inteiro [999para parar] "))
    if n == 999:
        break
    soma = soma + n
    cont += 1

print(f"Foram digitados {cont} números inteiros!")
print(f"A soma de todos os números digitados é {soma}!")