from time import sleep


print("-=-"*5)
print("    TABUADA    ")
print("-=-"*5)

t = 0
n = int(input("Digite o número que deseja saber a tabuada: "))

for c in range(1, 11):
    t = n * c
    print("{} x {:2} = {}".format(n, c, t))
    sleep(0.5)


"""tab = 0

n = int(input("Digite um número que deseja saber a sua tabuada: "))
for t in range(1, 11):
    tab = n * t
    print("{} x {:2} = {}".format(n, t, tab))
    sleep(1)"""

"""t = 0
n = int(input("Digite qual número você quer saber a tabuada: "))
for c in range(1, 11):
    t = n * c
    print("{} x {:2} = {}".format(n, c, t))"""
