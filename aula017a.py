# Aula 017 - Variável Composta do Tipo Lista (Parte 1)

lista = [2, 5, 9, 1]            # Cria uma lista                                    >> [2, 5, 9, 1]
lista[2] = 3                    # Altera o valor do elemento da posição 2           >> [2, 5, 3, 1]
lista.append(7)                 # Insere um elemento no final da lista              >> [2, 5, 3, 1, 7]
lista.sort()                    # Organiza os elementos em ordem crescente          >> [1, 2, 3, 5, 7]
lista.sort(reverse=True)        # Organiza os elementos em ordem decrescente        >> [7, 5, 3, 2, 1]
len(lista)                      # Retorna o tamanho da lista                        >> 5
lista.insert(2,2)               # Insere o valor 2 na posição 2                     >> [7, 5, 2, 3, 2, 1]
lista.pop()                     # Exclui o último elemento da lista                 >> [7, 5, 2, 3, 2]
lista.pop(2)                    # Exclui o valor da posição 2                       >> [7, 5, 3, 2]
lista.insert(0,2)               # Insere o valor 2 na posição 0                     >> [2, 7, 5, 3, 2]
lista.remove(2)                 # Exclui o primeiro valor 2 que aparece na lista    >> [7, 5, 3, 2]
lista2 = lista                  # Cria uma lista nova que está ligada a primeira (se alterar um valor em uma a outra também altera)
lista3 = lista[:]               # Cria uma cópia da lista mas não estão ligadas
print(lista)