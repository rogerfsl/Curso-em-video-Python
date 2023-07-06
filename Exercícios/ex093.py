jogador = {}
gols = []

jogador['nome'] = input("Nome do Jogador: ").strip().upper()
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p + 1}: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-=-' * 15)
print(jogador)
print('-=-' * 15)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=-' * 15)
print(f"O jogador {jogador['nome']} jogou {partidas} jogos!")

for g in range(len(gols)):
    print(f'    => Na partida {g +1}, fez {gols[g]} gols')
print(f'Foi um total de {sum(gols)}')

