print("-=-" * 10)
print("       RADAR ELETRÔNICO       ")
print("-=-" * 10)

print("O limite de velocidade da via é de 80km/h")
v = float(input("Digite a velocidade do carro em km: "))
multa = 0


if v > 80:
    print("Limite de velocidade excedido!")
    multa = (v - 80) * 7
    print("Por ter excedido o limite de velocidade deverá ser pago uma multa no valor de {}R$".format(multa))

print("Tenha um bom dia! Dirija com segurança!")
