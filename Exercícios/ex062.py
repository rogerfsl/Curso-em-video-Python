print("-=-"*10)
print(" SUPER PROGRESSÃO ARITIMÉTICA ")
print("-=-"*10)

pt = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
total = 0
total = 0
resp = 10

while resp != 0:
    total += resp
    while cont <= total:
        print(f'{pt} ->', end=' ')
        pt += r
        cont += 1
    print('Pause')
    resp = int(input('Quantos termos deseja ver a mais? '))
print(f'Progressão finalizada com {cont} termos mostrados!')
print('Fim!')

'''print("-=-"*10)
print(" SUPER PROGRESSÃO ARITIMÉTICA ")
print("-=-"*10)

pt = int(input('Digite o primeir termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
resp = 10
total = 0

while resp != 0:
    total += resp
    while cont <= total:
        print(f'{pt} ->', end=' ')
        pt += r
        cont += 1
        sleep(0.3)
    print('Pause...')
    sleep(0.5)
    resp = int(input('Quantos termos deseja saber a mais: '))
print('Fim do programa!')'''

'''pt = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
resp = 10
total = 0
while resp != 0:
    total += resp
    while cont <= total:
        print(f'{pt} ->', end=' ')
        pt += r
        cont += 1
    print('Pause')
    resp = int(input('Quantos termos deseja mostrar a mais: '))
print(f'Progressão finalizada com {cont} termos mostrados!')'''

'''pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
total = 0
mais = 10


while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{pt} ->', end=' ')
        pt += r
        cont += 1
    print('Pause')
    mais = int(input('Digite quantos termos você deseja ver a mais: '))

print(f'No total foram mostrados {cont} termos!')'''

'''pt = int(input("Digite o primeiro termo: "))
r = int(input('Digite a razão: '))
termo = pt
cont = 1
total = 0
resp = 10

while resp != 0:
    total += resp
    while cont <= total:
        print(f'{termo} ->', end=' ')
        termo += r
        cont += 1
    print('Pausa')
    resp = int(input("Quantos termos deseja mostrar a mais? "))

print(f'Progressão finalizada com {cont} termos mostrados!')'''











