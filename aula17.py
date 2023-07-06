numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = []

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros_pares.append(numeros[i])

print(numeros_pares)


"""nomes = []

while True:
    nome = input("Digite um nome [Digite sair para finalizar o programa] ").strip().lower()

    if nome in nomes:
        resp = input("Nome ja cadastrado! Deseja adicionar mesmo assim? [S | N]").strip().upper()
        if resp == 'N':
            nomes.remove(nome)
        while resp not in "SN":
            resp = input("Nome ja cadastrado! Deseja adicionar mesmo assim? [S | N]").strip().upper()

    if nome == 'sair':
        print("Programa finalizado!")
        break
    nomes.append(nome)

print(nomes)
print(len(nomes))

for i in range(len(nomes)):
    if nomes[i] == 'caio':
        print(f"O nome {nomes[i]} foi encontrado na posição {i}")
        break"""


'''for i in range(len(nomes)):
    if nomes[i] == 'caio':
        nomes[i] = 'Welson'

nomes.pop()
print(nomes)'''


"""a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f"Lista A {a}")
print(f"Lista B {b}")"""

"""valores = list()
for cont in range(0,5):
     valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Fim")"""

"""num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)

if 5 in num:
    num.remove(5)
else:
    print("Não achei o número 5")

print(num)
print(f"Essa lista tem {len(num)} elementos.")"""

