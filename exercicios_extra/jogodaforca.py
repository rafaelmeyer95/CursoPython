frase2 = []
frase3 = []
tentativas = []
erro = 0

frase = str(input('Digite uma palavra: ')).upper()

print('\n'*30)

for i in range(len(frase)):
    frase2.append(frase[i])
    frase3.append('_')


while True:
    letra = str(input('\nDigite uma letra: ')).upper()
    tentativas.append(letra)
    if letra not in frase:
        erro += 1
        print(f'Você pode errar mais {5-erro} vezes.\n')
    for p,l in enumerate(frase2):
        if letra == l:
            frase3[p] = letra

    for l in frase3:
            print(l,end='')

    if frase2 == frase3:
        print('\nParabéns, você ganhou!')
        break
    if erro == 5:
        print('\nVocê perdeu (5 erros)')
        print('Resposta: ',end='')
        for l in frase2:
            print(l,end='')
        break
    print('\nLetras:',tentativas)
