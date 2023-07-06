print("-----MAIOR E MENOR-----")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
menor = n1
# verificando o menor
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
# verificando o maior
maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
print("O menor número digitado foi {}".format(menor))
print("O maior número digitado foi {}".format(maior))


