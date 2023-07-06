def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda ='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaaum=10, taxared=5):
    print('-' * 30)
    print('RESUMO DOS PREÇOS'.center(30))
    print('-' * 30)
    print(f'Analisando o valor \t{moeda(preço)}')
    print(f'O dobro do preço: \t{dobro(preço, True)}')
    print(f'A metade do preço: \t{metade(preço, True)}')
    print(f'{taxaaum}% de aumento: \t{aumentar(preço, taxaaum, True)} ')
    print(f'{taxared}% de desconto: \t{diminuir(preço, taxared, True)}')
    print('-' * 30)
