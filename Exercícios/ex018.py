import math as mt

print("Descubra os valores do seno, cosceno e tangente de um ângulo! ")
ang = float(input("Digite o ângulo: "))

sen = mt.sin(mt.radians(ang))
cos = mt.cos(mt.radians(ang))
tang = mt.tan(mt.radians(ang))

print("O angulo de {} tem o seno de {:.2f}".format(ang, sen))
print("O angulo de {} tem o cosceno de {:.2f}".format(ang, cos))
print("O angulo de {} tem a tangente de {:.2f}".format(ang, tang))
