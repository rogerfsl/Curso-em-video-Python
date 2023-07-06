palavras = ('beringela', 'dado', 'fogo', 'amor', 'vogal', 'computador', 'piramide',
            "gratis", "programador")

for p in palavras:
    print(f" \nNa palavra {p.upper()} temos: ", end='')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
            