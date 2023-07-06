from time import sleep
print("-=-" * 10)
print("     SEQUÊNCIA FIBONACCI   ")
print("-=-" * 10)

n = int(input('Digite quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'→ {t3}', end=' ')
    cont += 1
    t1 = t2
    t2 = t3
    sleep(0.5)
sleep(0.5)
print('→ FIM!')



'''n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    sleep(0.5)
    print(f'→ {t3}', end=' ')
    cont += 1
    t1 = t2
    t2 = t3
sleep(1)
print('→ Fim')'''

'''n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('_'*36)
print(f'{t1} → {t2}', end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    sleep(0.5)
    print(f'→ {t3}', end=' ')
    cont += 1
    t1 = t2
    t2 = t3
sleep(1)
print('→ FIM!')'''
