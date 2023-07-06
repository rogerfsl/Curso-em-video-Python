print("-=-"*8)
print("   10 TERMOS DE UMA PA   ")
print("-=-"*8)

pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
dec = pt + (10-1) * r

for c in range(pt, dec + r, r):
    print("{}".format(c), end=" -> ")
print("ACABOU!!!")


"""pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
dec = pt + (10-1) * r

for c in range(pt, dec + r, r):
    print(c, end=" -> ")
print("Acabou")"""
