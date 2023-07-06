from datetime import date


print('ALISTAMENTO MILITAR')

#variaveis
nasc = int(input("Digite o ano em que você nasceu: "))
ano = date.today().year
idade = ano - nasc

#programa
print("Quem nasceu em {} tem {} anos em {} ".format(nasc, idade, ano))

if idade < 18:
    faltanos = 18 - idade
    print("Ainda faltam {} anos para você se alistar.".format(faltanos))
    print("Seu alistamento será em {}".format(ano + faltanos))
elif idade == 18:
    print("Você deve efetuar o alistamento". format(idade))
else:
    faltanos = idade - 18
    print("Passaram {} anos do seu alistamento obrigatorio!".format(faltanos))
    print("O seu alistamento foi em {}".format(ano - faltanos))
