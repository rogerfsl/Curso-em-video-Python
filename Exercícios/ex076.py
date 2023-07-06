produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90, "Cola", 11.35)

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)

for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<40} R${produtos[c+1]:>7.2f}')

print('-'*50)
"""for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<41}", end='')
    else:
        print(f"R${produtos[pos]:>7.2f}")"""

'''for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<40}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')'''



'''for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<40}', end=' ')
    else:
        print(f'R${produtos[pos]:>7.2f}')'''

'''for pos in range(0, len(produtos), 2):
    print(f'{produtos[pos]:.<41}R${produtos[pos + 1]:>7.2f}')'''

'''for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<40}', end=' ')
    else:
        print(f'R${produtos[c]:>7.2f}')'''

"""for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<41}R${produtos[c +1]:>7.2f}')"""

'''for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<41}', end='')
    else:
        print(f'R${produtos[c]:>7.2f}')'''

"""for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<41}", end='')
    else:
        print(f"R${produtos[pos]:>7.2f}",)"""

'''for pos in range(0, len(produtos), 2):
    print(f"{produtos[pos]:.<41}R${produtos[pos+1]:>7.2f}")'''