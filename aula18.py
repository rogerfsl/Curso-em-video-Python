galera = []
dado = []
maior = menor = 0
for c in range(0, 3):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f"{p[0]} é maior de idade!")
        maior += 1
    else:
        print(f"{p[0]} é menor de idade")
        menor += 1

print(f"Temos {maior} maiores e {menor} menores de idade!")

'''galera = [['João', 19], ["Ana", 33], ['Joaquim', 13], ['Maria, 45']]
for p in galera:
    print(p)'''

"""teste = ['Gustavo', 40]
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)"""
