frase = str(input("Digite uma frase: ")).strip().lower()
frase = frase.replace("ã", "a")
frase = frase.replace("á", "a")
frase = frase.replace("à", "a")
pa = frase.find("a")
ua = frase.rfind("a")
print("A letra A aparece {} vezes.".format(frase.count("a")))
print("A letra A aparece primeiro na posição {}.".format(pa + 1))
print("A letra A apareçe por último na posição {}".format(ua + 1))


#frase = str(input("Digite uma frase: ")).strip().lower()
#print("A letra A aparece {} vezes na frase.".format(frase.count("a")))
#print("A letra A aparece pela primeira vez na posição {}.".format(frase.find("a")+1))
#print("A letra A aparece pela última vez na posição {}.".format(frase.rfind("a")+1))