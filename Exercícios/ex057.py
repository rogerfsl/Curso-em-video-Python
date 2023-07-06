s = input("Digite o seu sexo: [M/F] ").strip().upper()[0]
while s not in "MF":
    s = input("OPÇÃO INVÁLIDA! Por favor, digite o seu sexo: [M/F] ").strip().upper()[0]

print(f"Sexo {s} registrado com sucesso!")


'''s = input("Informe seu sexo: [M/F] ").strip().upper()[0]
while s not in "MF":
    s = input("Opção invalida! Por favor, informe o seu sexo: [M/F] ").strip().upper()[0]
print(f'Sexo {s} registrado com sucesso!')'''

"""s = ''
while s != 'F' or s != 'M':
    s = input("Digite o sexo de uma pessoa: [M/F] ").upper().strip()
    if s == 'F' or s == 'M':
        print("Tudo certo!")
        break
    else:
        print("Digite uma opção Válida!")"""
