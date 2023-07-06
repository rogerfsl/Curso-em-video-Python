print("-=-" * 8)
print("    CAIXA ELETRÔNICO   ")
print("-=-" * 8)

valor = int(input('Digite o valor que seseja sacar: '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0

        if total == 0:
            break
print('VOLTE SEMPRE!')


'''valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0

        if total == 0:
            break
print('VOLTE SEMPRE!')'''


