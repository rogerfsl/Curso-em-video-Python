from random import randint


aleatorio = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),\
            randint(0, 10)

print(f"Esses foram os números gerados aleatoriamente:  ", end='')

for c in aleatorio:
    print(c, end=' ')

print(f"\nO maior número gerado foi: {max(aleatorio)}")
print(f"O menor número criado foi: {min(aleatorio)}")

"""print('Os valores sorteados foram: ', end='')
for n in aleatorio:
    print(f'{n}  ', end='')

print('\nO maior valor sorteado foi {}.'.format(max(aleatorio)))
print('O menor valor sorteado foi {}.'.format(min(aleatorio)))"""
