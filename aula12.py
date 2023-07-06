nome = str(input("Qual é o seu nome? "))
if nome == "Welson":
    print("Que nome foda!")
elif nome == "Matheus" or nome == "Enzo" or nome == "Valentina":
    print("Seu nome é bem popular no brasil.")
elif nome in "Ana Claudia Jessica Juliana":
    print("Que belo nome a Senhorita tem!")
else:
    print("Seu nome é bem normal!")
print(f"Tenha um bom dia {nome}")

