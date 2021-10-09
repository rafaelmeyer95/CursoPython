# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar as notas de caada aluno individualmente.

alunos = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1]+aluno[2])/2)
    alunos.append(aluno[:])
    aluno.clear()
    continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break
alunos.sort()

print(41*'-')
print('Nº Chamada          Nome          Média'.upper())
print(41*'-')
for i in range(len(alunos)):
    print(f'{i+1:^12}{alunos[i][0]:^20}{alunos[i][3]:^9}'.title())
print(41*'-')

while True:
    num = int(input('Mostrar notas de qual aluno? (0 para sair) '))
    if num == 0:
        break
    print(f'As notas de {alunos[num-1][0]} foram:\nNota 1: {alunos[num-1][1]}\nNota 2: {alunos[num-1][2]}')
