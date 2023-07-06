print("-=-"*10)
print("    CONSULTA DE EMPRÉSTIMO!   ")
print("-=-"*10)

valorCasa = float(input("Digite o valor da casa: R$ "))
sal = float(input("Digite o salário do comprador: R$ "))
temp = int(input("Em quantos anos será pago o empréstimo? "))
prest = valorCasa / (temp * 12)
porcent = sal * 30 / 100


if prest > porcent:
    print("Para pagar uma casa no valor de R$ {:.2f} em {} anos, ".format(valorCasa, temp), end="")
    print("a prestação sera no valor de R$ {:.2f}".format(prest))
    print("EMPRÉSTIMO NEGADO")
elif prest <= porcent:
    print("Para pagar uma casa no valor de R$ {:.2f} em {} anos, ".format(valorCasa, temp), end="")
    print("a prestação sera no valor de R$ {:.2f}".format(prest))
    print("EMPRÉSTIMO CONCEDIDO")
