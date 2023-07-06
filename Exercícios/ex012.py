print("Qual é o valor do produto com desconto?")
p = float(input("Digite o valor do produto? R$ "))
d = (p * 5)/100
print("O produto vale R$ {:.2f} e com desconto de 5% seu preço vai para R$ {:.2f}".format(p, p - d))