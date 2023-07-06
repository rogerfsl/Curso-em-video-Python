from time import sleep

print("-=-" * 9)
print("   CADASTRO DE PRODUTOS  ")
print("-=-" * 9)

totgast = menorprec = totmil = cont = 0
menorprod = ' '

while True:
    n = input('Digite o nome do produto: ').strip()
    p = float(input('Digite o preço do produto: R$'))
    totgast += p
    cont += 1

    if p >= 1000:
        totmil += 1

    if cont == 1:
        menorprec = p
        menorprod = n
    else:
        if p < menorprec:
            menorprec = p
            menorprod = n

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()

    if resp == 'N':
        print('Obrigado pela preferência e tenha um bom dia!')
        sleep(0.5)
        break

print(f'Foram comprados {cont} produtos custando R${totgast:.2f}')
print(f'No total {totmil} produtos custaram mais de R$1000,00 reais ')
print(f'E o produto mais barato foi {menorprod}, custando R${menorprec:.2f}')
