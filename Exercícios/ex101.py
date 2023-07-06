def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('-' * 35)
nasc = int(input('Digite o ano de nascimento: '))
print(voto(nasc))

"""def voto(idade):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif 16 >= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


print('-' * 30)
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
"""
