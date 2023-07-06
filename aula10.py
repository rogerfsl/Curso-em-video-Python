# nome = str(input("Qual é o seu nome? "))
# print("Bom dia, {}!".format(nome))
# if nome == "Roger":
#    print("Que belo nome você tem!")
# else:
#    print("Seu nome é tão comum!")

nome = str(input("Digite o nome do aluno: "))
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("A média do aluno {} é {:.1f}.".format(nome, m))
if m >= 6.0:
    print("O aluno {}, está aprovado!".format(nome))
else:
    print("O aluno {}, está de recuperação!".format(nome))

