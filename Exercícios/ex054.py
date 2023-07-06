from datetime import date

print("-=-"*8)
print("   CONTADOR DE IDADE   ")
print("-=-"*8)

atual = date.today().year
idade = 0
cont1 = 0
cont2 = 0

for i in range(1, 8):
    nasc = int(input("Digite a sua data de nascimento da {}ª pessoa: ".format(i)))
    idade = atual - nasc
    if idade < 21:
        cont1 += 1
    else:
        cont2 += 1
print("Ao todo tivemos {} pessoas maiores de idade!".format(cont1))
print("E também tivemos {} pessoas menores de idade!".format(cont2))



"""ano = date.today().year
cont = 0
cont2 = 0

for i in range(1, 8):
    nasc = int(input("Digite a sua data de nascimento da {}ª pessoa: ".format(i)))
    idade = ano - nasc
    if idade >= 18:
        cont = cont + 1
    elif idade < 18:
        cont2 = cont2 + 1
print("{} pessoas já atingiram a maioridade!".format(cont))
print("{} Pessoas ainda não atingiram a maioridade!".format(cont2))"""
