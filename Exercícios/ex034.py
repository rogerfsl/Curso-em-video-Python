print("---AUMENTO SALARIAL---")

sal = float(input("Digite o valor do salário do funcionario R$ "))
aum = 0

if sal <= 1250:
    aum = sal * 15 / 100
    print("O salário atual do funcionário é R$ {:.2f} e com aumento vai para R$ {:.2f}.".format(sal, sal + aum))
else:
    aum = sal * 10 / 100
    print("O salario atual do funcionáro é R$ {:.2f} e com aumento vai para R$ {:.2f}.".format(sal, aum + sal))

