tabela = 'Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', \
         'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', \
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO'

print("-" * 40)
print(f"Os cinco primeiro colocados são: {tabela[:5]}")
print("-" * 40)
print(f"Os 4 últimos colocados são: {tabela[-4:]}")
print("-" * 40)
print("A tabela em ordem alfabética fica assim: ", end='')
print(sorted(tabela))
print("-" * 40)
print(f"A chapecoense está na {tabela.index('Chapecoense')+1}ª colocação.")
print("-" * 40)



""""print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print(f'\nOs 4 últimos colocados são: {tabela[-4:]}')
print('\nOs times em ordem alfabética são: ', end='')
print(sorted(tabela))
print('\nA Chapecoense está na {} colocação'.format(tabela.index('Chapecoense')+1))"""
