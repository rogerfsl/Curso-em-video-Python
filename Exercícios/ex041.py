from datetime import date

print("-=-" * 12)
print("      CAMPEONATO DE NATAÇÃO.      ")
print("DEFINA A CATEGORIA DOS COMPETIDORES.")
print("-=-" * 12)

idade = int(input("Digite o ano de nascimento do competidor: "))
at = date.today().year
cat = at - idade


if cat <= 9:
    print("O atleta tem {} anos.".format(cat))
    print("O atleta está na categoria MIRIM.")
elif 9 < cat <= 14:
    print("O atleta tem {} anos.".format(cat))
    print("O atleta está na categoria INFANTIL.")
elif 14 < cat <= 18:
    print("O atleta tem {} anos.".format(cat))
    print("O atleta está na categoria JUNIOR.")
elif 19 <= cat <= 30:
    print("O atleta tem {} anos.".format(cat))
    print("O atleta está na categoria ADULTO.")
elif cat >= 31:
    print("O atleta tem {} anos.".format(cat))
    print("O atleta está na categoria MASTER.")
print("DESEJAMOS A TODOS UM ÓTIMO CAMPEONATO")






