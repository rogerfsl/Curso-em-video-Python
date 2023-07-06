print("-----PREÇO DA PASSAGEM-----")

d = float(input("Digite a distância da viagem desejada: "))

if d <= 200:
    p = d * 0.50
    print("Você esta prestes a começar uma viagem de {:.1f} km.".format(d))
    print("E o valor da passagem é R$ {:.2f}.".format(p))
else:
    p = d * 0.45
    print("Você esta prestes a começar uma viagem de {:.1f} km.".format(d))
    print("E o valor da passagem é R$ {:.2f}.".format(p))
print("Tenha uma boa viagem!")