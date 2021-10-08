# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
# se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressão = str(input('Digite a expressão: '))
lista = []
erro = 0

for símbolo in expressão:
    if símbolo == '(':
        lista.append(1)
    elif símbolo == ')':
        if 1 in lista:
            lista.pop()
        else:
            erro = 1
            break
if lista == [] and erro == 0:
    print('Expressão Válida')
else:
    print('Expressão Inválida')
