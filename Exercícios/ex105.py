
def notas(*n, sit=False):
    """
    -> função para analidar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação
    :return: dicionários com as informalçoes sobre a situação da turma.
    """
    aluno = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    if sit:
        if aluno['media'] >= 9:
            aluno['situação'] = 'EXCELENTE'
        elif aluno['media'] >= 7:
            aluno['situação'] = 'BOA'
        elif aluno['media'] >= 6:
            aluno['situação'] = 'Razoável'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(5.5, 5.5, 8, sit=True)
print(resp)
help(notas)