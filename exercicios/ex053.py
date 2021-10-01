from unidecode import unidecode

frase = str(input('Digite uma frase: '))

frase = frase.upper()
frase = frase.replace(' ','')
frase = unidecode(frase)
frase2 = frase[::-1]

print(frase)
print(frase2)

if frase == frase2:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindrimo')
