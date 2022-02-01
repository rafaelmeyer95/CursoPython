# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

def notas(* num, sit=False):
    """
    A função notas recebe várias notas como entrada e mostra a análise da turma
    :param num: Notas dos alunos
    :param sit: (opcional) Mostra a situação da turma
    :return: Retorna um dicionário com a análise das notas e a situação (opcional)
    """
    if sum(num)/len(num) < 5:
        situacao = 'Pessima'
    elif sum(num)/len(num) < 7:
        situacao = 'Ruim'
    elif sum(num)/len(num) < 9:
        situacao = 'Boa'
    else:
        situacao = 'Otima'

    if sit == True:
        dados = {'total':len(num),'maior':max(num),'menor':min(num),'media':sum(num)/len(num),'situação':situacao}
    else:
        dados = {'total': len(num), 'maior': max(num), 'menor': min(num), 'media': sum(num)/len(num)}
    return dados

            # Programa Principal
resp = notas(6, 8, 5, 9,sit=True)
print(resp)