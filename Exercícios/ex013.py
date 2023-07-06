print("Reajuste salarial")
s = float(input("Digite o valor do salário: R$ "))
ns = s * 15/100
print("O salario atual do funcionário é de R$ {:.2f} e com aumento de 15% vai para R$ {:.2f}".format(s, ns + s ))
