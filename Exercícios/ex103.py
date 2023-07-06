def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-=-' * 20)
n = input('Nome do jogador: ').strip()
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)

