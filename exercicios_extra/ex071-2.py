quantia = 0

senha = int(input('Olá, digite sua senha: '))

while True:
    if senha == 2021:
        opcao = int(input('\nOpções:\n(1) Depósito\n(2) Saque\n'.upper()))
        if opcao == 1:
            valor = int(input('\nQual valor deseja depositar?'))
            quantia += valor
            print(f'\nDepósito realizado com sucesso!\nSaldo Atual: {quantia}\n')
            continua = str(input('Deseja realizar outra operação? [S/N] '))
            if continua in 'Nn':
                break
        elif opcao ==2:
            print(f'\nSaldo: {quantia}')
            valor = int(input('Digite o valor a ser sacado: '))
            if valor > quantia:
                print('Saldo insuficiente')
                continua = str(input('Deseja realizar outra operação? [S/N] '))
                if continua in 'Nn':
                    break
            else:
                ced100 = valor // 100
                ced50 = (valor - (ced100 * 100)) // 50
                ced20 = (valor - (ced100 * 100 + ced50 * 50)) // 20
                ced10 = (valor - (ced100 * 100 + ced50 * 50 + ced20 * 20)) // 10
                ced1 = valor - (ced100 * 100 + ced50 * 50 + ced20 * 20 + ced10 * 10)
                quantia -= valor
                print(f'\n{ced100} cédulas de R$100,00\n{ced50} cédulas de R$50,00\n{ced20} cédulas de R$20,00\n{ced10} cédulas de R$10,00\n{ced1} cédulas de R$1,00\n\nSaldo Atual: {quantia}')
                continua = str(input('\nDeseja realizar outra operação? [S/N] '))
                if continua in 'Nn':
                    break
    else:
        senha = int(input('Senha inválida!\nDigite novamente: '))