expr = input("Digite uma expressão: ")
pilha = []

for simb in expr:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")

if len(pilha) == 0:
    print("Expressão correta!")
else:
    print("Expressão incorreta!")
