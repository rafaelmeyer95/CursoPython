frase = """Curso
em Vídeo
Python"""          #Utilizar três aspas permite pular a linha

#FATIAMENTO
print(frase[6])                 #Printa o caracter que ocupa a posição 5
print(frase[9:14])              #Printa os caracteres da posiçao 9 à 13
print(frase[9:21:2])            #Printa os caracteres da posição 9 à 20 (de 2 em 2)
print(frase[:5])                #Printa os caracteres da primeira posição até a posição 4
print(frase[15:])               #Printa os caracteres da posição 15 até a última
print(frase[9::3])              #Printa os caracteres da posição 9 até o final (de 3 em 3)

#ANÁLISE
print(len(frase))               #Tamanho da frase
print(frase.count('o'))         #Conta quantas vezes aparece a letra "o"
print(frase.count('o',0,13))    #Conta quantas vezes aparece a letra "o" entre a posição 0 e 12
print(frase.find('deo'))        #Mostra a posição onde aparece a palavra "deo"
print(frase.find('Android'))    #Retorna o resultado "-1" que é uma posição inexistente, notificando que essa palavra não existe na frase
print('Curso' in frase)         #Retorna "True" informando que a palavra existe dentro da frase
print(frase.find('Vídeo'))      #Retorna a posição em que a palavra "Vídeo" se encontra

#TRANSFORMAÇÃO
frase.replace('Python','Android')           #Substitui momentaneamente a palavra "Python" pela palavra "Android"
frase = frase.replace('Python','Android')   #Substitui e salva a palavra "Python" pela palavra "Android"
frase.upper()           #Transforma todas as letras minúsculas em maiúsculas
frase.lower()           #Transforma todas as letras maiúsculas em minúsculas
frase.capitalize()      #Transforma apenas a primeira letra da frase em maiúscula e o resto em minúscula
frase.title()           #Transforma apenas as letras iniciais das palavras em maiúsculas e o resto em minúscula
frase.strip()           #Remove todos os espaços "inúteis" (à esquerda e a direita)
frase.rstrip()          #Remove apenas os espaços "inúteis" do lado direito
frase.lstrip()          #Remove apenas os espaços "inúteis" do lado esquerdo

#DIVISÃO
frase.split()               #Divide a frase em uma lista (Separa as palavras)
dividido = frase.split()    #Cria a variável "dividido" com a lista
print(dividido[0][2])       #Printa o caracter 2 da palavra 0 da lista "dividido"

#JUNÇÂO
'-'.join(frase)     #Junta todos os elementos de uma lista e separa pelo caracter "-"
