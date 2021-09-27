nome = str(input('Digite seu nome completo:\n')).strip()

print('Seu nome em maiúsculas é:',nome.upper())
print('Seu nome em minúsculas é:',nome.lower())
print('Seu nome possui {} letras.'.format(len(nome.replace(' ',''))))

lista = nome.split()

for i in range (len(lista)):
    print('O seu {}º nome é {} e possui {} letras.'.format(i+1,lista[i],len(lista[i])))

