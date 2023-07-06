print("-=-"*8)
print("   10 TERMOS DE UMA PA   ")
print("-=-"*8)

pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1

while cont <= 10:
    print(f'{pt} -> ', end=' ')
    pt += r
    cont += 1
print('Acabou!')


'''pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1

while cont <= 10:
    print(f'{pt} ->', end=' ')
    pt += r
    cont += 1

print('Fim!')'''

'''pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1

while cont <= 10:
    print(f'{pt} ->', end=' ')
    pt += r
    cont += 1

print('FIM!')'''

'''pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
termo = pt
cont = 1

while cont <= 10:
    print(f'{termo} ->', end=' ')
    termo += r
    cont += 1
print('Fim!')'''

'''pt = int(input("Digite o primeiro termo de uma PA: "))
r = int(input("Digite o a razão: "))
termo = pt
c = 1

while c <= 10:
    print(f'{termo} ->', end=" ")
    termo += r
    c += 1

print('FIM')'''
