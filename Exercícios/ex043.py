print("CÁLCULO DE IMC")

nome = str(input("Digite o seu nome: "))
peso = float(input("Digite o seu peso em quilos: "))
alt = float(input("Digite a sua altura: "))
imc = peso / (alt ** 2)

if imc < 18.5:
    print("Olá {}, seu imc é de {:.1f} ".format(nome, imc), end="")
    print("e você está abaixo do peso ideal!")
elif 18.5 <= imc < 25:
    print("Olá {}, seu imc é de {:.1f} ".format(nome, imc), end="")
    print("e você está no peso ideal!")
elif 25 <= imc < 30:
    print("Olá {}, seu imc é de {:.1f} ".format(nome, imc), end="")
    print("e você está com sobrepeso!")
elif 30 <= imc < 40:
    print("Olá {}, seu imc é de {:.1f} ".format(nome, imc), end="")
    print("e você está com obesidade!")
elif imc >= 40:
    print("Olá {}, seu imc é de {:.1f} ".format(nome, imc), end="")
    print("e você está com obesidade mórbida!")


