import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é R${moedas.metade(p)}')
print(f'O dobro de {p} é R${moedas.dobro(p)}')
print(f'Aumentando 10%, temos R${moedas.aumentar(p, 10)}')
print(f'Diminindo 13%, temos R${moedas.diminuir(p, 13)}')


