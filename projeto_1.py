menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Opção: '''

LIMITE = 500
LIMITE_SAQUES = 3

extrato = ''
saldo = 0
numero_saques = 0

while True:

    opcao = input(menu)

    if opcao == '1':
        print('Deposito')

        try:
            valor = float(input('Quantia: '))

            if valor <= 0:
                print('Apenas valores maiores do que 0 são permitidos.')
            else:
                saldo += valor
                extrato += f'Deposito de R${valor:.2f}\n'

        except ValueError:
            print('Apenas valores numericos são permitidos.')
    
    elif opcao == '2':
        print('Saque')

        if numero_saques >= LIMITE_SAQUES:
            print('Limite de saque diário atingido.')
            
        else:
            
            try:
                valor = float(input('Quantia: '))

                if valor <= 0:
                    print('Apenas valores maiores do que 0 são permitidos.')

                elif valor <= LIMITE:
                    
                    if valor > saldo:
                        print('Saldo insuficiente.')
                    else:
                        saldo -= valor
                        numero_saques += 1
                        extrato += f'Saque    de R${valor:.2f}\n'
                else:
                    print('O valor do saque é maior do que o limite de R$500 por saque.')
                
            except ValueError:
                 print('Apenas valores numericos são permitidos.')

    elif opcao == '3':
        print('Extrato')
        print(extrato)
        print(f'Saldo:      R${saldo:.2f}')

    elif opcao == '0':
        print('Sair')
        break

    else:
        print('Operação inválida, por favor selecione novament a operação desejada.')