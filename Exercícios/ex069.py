print("-=-" * 9)
print("   CADASTRO DE PESSOAS  ")
print("-=-" * 9)

totp = toth = totm = 0

while True:
    print('CADASTRO')
    id = int(input('Idade: '))

    s = ' '
    while s not in 'MF':
        s = input('Sexo: [M/F] ').strip().upper()[0]

    if id > 18:
        totp += 1

    if s in 'Mm':
        toth += 1
    elif s in 'Ff' and id < 20:
        totm += 1

    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]

    if escolha in 'Nn':
        break

print(f'Total de pessoas com mais de 18 anos: {totp}')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totm} mulher com menos de 20 com menos de 20 anos.')
