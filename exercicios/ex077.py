# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve
# mostrar, para cada palavra, quais são as suas vogais.

tupla = ('recreio','alfabeto','merendar','rafael','antonio','guanabara','curso','em','video','python')

for palavra in tupla:
    print(f'\nNa palavra {palavra} temos as vogais: ',end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra,end=' ')