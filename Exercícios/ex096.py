def área(l, c):
    a = l * c
    print(f'A área de um terreno com {l} x {c} é de {a}m².')


print('--   Controle de terreno    --')
print('-' * 30)

l = float(input("Largura (m): "))
c = float(input('Cumprimento (m): '))
área(l, c)
