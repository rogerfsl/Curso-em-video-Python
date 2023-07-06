import math as mt

print("Descubra a hipotenusa!")
cato = float(input("Digite o valor do cateto oposto: "))
cata = float(input("Digite o valor do cateto adjascente: "))
#hipo = mt.sqrt((cato*cato) + (cata*cata))
hipo = mt.hypot(cato, cata)
print("A hipotenusa desse triangulo é {:.2f} ".format(hipo))