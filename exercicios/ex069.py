# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
# a) Quantas pessoas tem mais de 18 anos
# b) Quantos homens foram cadastrados
# c) Quantas mulheres tem menos de 20 anos

maioridade = homens = novinha = 0

while True:
    print(40*'-')
    print('deseja cadastrar uma nova pessoa? [S/N]'.upper())
    print(40*'-')
    resposta = str(input(''))
    if resposta in 'Nn':
        break
    if resposta in 'Ss':
        idade = int(input('Qual a idade da pessoa? '))
        sexo = str(input('Qual o sexo da pessoa? [M/F]'))
        if sexo in 'FfMm':
            if idade > 17:
                maioridade += 1
            if sexo in 'Ff':
                if idade < 20:
                    novinha += 1
            if sexo in 'Mm':
                homens += 1
        else:
            print('Entrada inválida')
    else:
        print('Entrada inválida!')
print(f'Dentro das pessoas cadastradas {maioridade} já atingiram a maioridade, {homens} são homens e {novinha} são mulheres com menos de 20 anos!')