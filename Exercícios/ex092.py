from datetime import date
ano_atual = date.today().year
apos = 0
infos = {}

infos['nome'] = input("Nome: ").strip()
infos['idade'] = (int(input("Ano de Nascimento: ")) - ano_atual) * -1
infos['ctps'] = int(input("Carteira de trabalho (0 não tem): "))

if infos['ctps'] != 0:
    infos['contratação'] = int(input("Ano de Contratação: "))
    infos['salário'] = float(input("Salário: R$ "))
    apos = 35 - (ano_atual - infos['contratação'])
    infos['Aposentadoria'] = infos['idade'] + apos
print('-=-' * 20)
for k, v in infos.items():
    print(f'{k} tem valor {v}')




