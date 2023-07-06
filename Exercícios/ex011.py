print("Quantos litros de tinta são necessarios para pintar essa parede?")
a = float(input("Qual a altura da parede? "))
l = float(input("Qual a largura da parede? "))
ar = a * l
print ("A area da parede é {}m² e vão ser necessarios {} litros de tinta para pintar ela.". format(ar, ar/2))
