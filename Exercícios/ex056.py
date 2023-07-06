print("-=-" * 8)
print("  ANALISADOR COMPLETO! ")
print("-=-" * 8)

somaidade = 0
hmaisvelho = 0
nvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f"----------{p}ª PESSOA----------")
    nome = input("Nome: ").strip().upper()
    id = int(input("Idade: "))
    sex = input("Sexo [M/F]: ").strip().upper()
    somaidade += id
    if p == 1 and sex == "M":
        hmaisvelho = id
        nvelho = nome
    if sex == "M" and id > hmaisvelho:
        hmaisvelho = id
        nvelho = nome
    if sex == "M" and id < 20:
        totmulher20 += 1


print(f"A media de idade do grupo é de {somaidade / 4} anos!")
print(f"O homem mais velho tem {hmaisvelho} e se chama {nvelho}!")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos!")



"""medid = 0
conth = 0
hvelho = ''
contm = 0

for p in range(1, 5):
    nome = input(f"Digite o nome da {p}ª pessoa: ").upper()
    id = int(input(f"Digite a idade da {p}ª pessoa: "))
    sex = input(f"Digite o sexo da {p} pessoa [M\F]: ").upper().strip()
    medid += id
    if id > conth and sex == "M":
        conth = id
        hvelho = nome
    else:
        if id < 20 and sex == "F":
            contm += 1

print(f"A média de idade do grupo é {medid / 4}!")
print(f"O homem mais velho tem {conth} anos e se chama {hvelho}!")
print(f"No total existem {contm} mulheres com menos de 20 anos!")"""

"""medid = 0
contm = 0
conth = 0
hvelho = ''

for n in range(1, 5):
    nome = input("Digite o nome da {}° pessoa: ".format(n)).strip().upper()
    id = int(input("Digite a idade da {}° pessoa: ".format(n)))
    sex = input("Digite o sexo da {}° pessoa [M\F]: ".format(n)).strip().upper()
    medid += id
    if id > contm and sex == "M":
        contm = id
        hvelho = nome
    else:
        if id < 20 and sex == "F":
            conth += 1

print("A idade media do grupo é: {:.1f}. ".format(medid / 4))
print("O homem mais velho tem {} anos e ele se chama {}.".format(contm, hvelho))
print("Existem {} mulheres com menos de 20 anos.".format(conth))"""
