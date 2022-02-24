from time import sleep

nomes = []
idades = []

def menu():

    while True:
        print('-'*40)
        print('menu principal'.upper().center(40))
        print('-' * 40)
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova Pessoa')
        print('3 - Sair do Sistema')
        print('-' * 40)

        while True:
            try:
                opcao = int(input('Sua Opcao: '))
            except:
                print('-' * 40)
                print('Digite uma opção válida!')
                print('-' * 40)
            else:
                break

        if opcao == 1:
            print('-' * 40)
            print('Nome'.center(20),end='')
            print('Idade'.center(20))
            print('-' * 40)
            for i in range(len(nomes)):
                print(f'{nomes[i]}'.title().center(20),end='')
                print(f'{idades[i]}'.center(20))
        elif opcao == 2:
            print('-' * 40)
            while True:
                try:
                    ficha(input('Nome: '), int(input('Idade: ')))
                except:
                    print('-' * 40)
                    print('Digite uma idade válida!')
                    print('-' * 40)
                else:
                    break
            print('-' * 40)
        elif opcao == 3:
            print('-' * 40)
            print('Saindo do Sistema.... Ate Logo!'.center(40))
            print('-' * 40)
            sleep(2)
            break
        else:
            print('-' * 40)
            print('Digite uma opção válida!')
            print('-' * 40)

def ficha(nome,idade):
    nomes.append(nome)
    idades.append(idade)


