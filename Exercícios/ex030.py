print("=" * 16)
print("  PAR OU IMPAR  ")
print("=" * 16)

n = int(input("Digite um número: "))

if n % 2 == 0:
    print("O número {} é par!".format(n))
else:
    print("O número {} é impar!".format(n))
