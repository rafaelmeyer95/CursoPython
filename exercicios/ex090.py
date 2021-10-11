# Faça um programa que leia nome emédia de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))

if dados['media'] < 4:
    dados['situacao'] = 'Reprovado'
elif 4 <= dados['media'] < 7:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'Aprovado'

print(30*'-')
for k,v in dados.items():
    print(f'{k}: {v}'.title())


