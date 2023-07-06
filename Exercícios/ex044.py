print(f'{"Lojas Gunabara":=^40}')



preço = float(input("Digite o valor do produto desejado: R$ "))

print("""Escolha a forma de pagamento :
[1] PARA DINHEIRO OU PIX (10% DE DESCONTO)
[2] PARA PAGAMENTO A VISTA NO DÉBITO (5% DE DESCONTO)
[3] PARA PAGAMENTO A VISTA NO CRÉDITO (PREÇO NORMAL)
[4] PARA PAGAMENTO PARCELADO EM 2 VEZES (ACRÉSCIMO DE 10% DE JUROS)
[5] PARA PAGAMENTO PARCELADO EM 3 VEZES OU MAIS (ACRÉSCIMO DE 20% DE JUROS)""")

pag = int(input("Digite a forma de pagamento: "))

if pag == 1:
    desc = preço * 10/100
    print("O preço do seu produto é R$ {:.2f} e com desconto de 10% foi para R$ {:.2f}.".format(preço, preço - desc))
elif pag == 2:
    desc = preço * 5/100
    print("O preço do seu produto é R$ {:.2f} e com desconto de 5% foi para R$ {:.2f}.".format(preço, preço - desc))
elif pag == 3:
    print("O preço do seu produto é R$ {:.2f}.".format(preço))
elif pag == 4:
    jur = preço * 10/100
    print("A sua compra será parcelada em 2x de R${:.2f}".format((preço + jur) / 2))
    print("O preço do seu produto é R$ {:.2f} e com acréscimo de 10% foi para R$ {:.2f}.".format(preço, preço + jur))
elif pag == 5:
    jur = preço * 20/100
    parc = int(input("Quantas Parcelas? "))
    print("A sua compra será parcelada em {} de R${:.2f}".format(parc, (preço + jur) / parc))
    print("O preço do seu produto é R$ {:.2f} e com acréscimo de 20% foi para R$ {:.2f}".format(preço, preço + jur))
else:
    print("OPÇÃO INVÁLIDA, VOLTE E DIGITE UM NÚMERO DE 1 A 5!")
