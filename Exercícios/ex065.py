n = 0
resp = 'S'
cont = 0
media = 0
maior = menor = 0

while resp == 'S':

    n = int(input("Digite um número inteiro: "))
    cont += 1
    media = media + n

    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    resp = input("Deseja continuar? [S/N] ").upper().strip()[0]

print(f'Foram digitados {cont} números inteiros!')
print(f'A media dos números digitados é {media / cont :.1f}.')
print(f'O maior número digitado foi {maior} e o menor foi {menor}.')
