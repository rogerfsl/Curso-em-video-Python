print("AVALIAÇÃO FINAL")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2

if m < 5:
    print("A média do aluno é {}".format(m))
    print("O ALUNO ESTÁ REPROVADO!")
elif 5 <= m <= 6.9:
    print("A média do aluno é {}".format(m))
    print("O ALUNO ESTÁ DE RECUPERAÇÃO")
else:
    print("A media do aluno é {}".format(m))
    print("O ALUNO ESTÁ APROVADO! PARABENS!!")
