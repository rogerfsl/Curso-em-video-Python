import random as rd

print("Quem vai apagar o quadro? ")

a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno: "))
a3 = str(input("Digite o nome do terceiro aluno: "))
a4 = str(input("Digite o nome do quarto aluno: "))

lista_alunos = [a1, a2, a3, a4]
escolhido = rd.choice(lista_alunos)

print("O aluno escolhido foi {}".format(escolhido))