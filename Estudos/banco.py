import os


menu = """
Bem vindo ao menu do Banco Central

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

Escolha uma das opções: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu).upper() #Roda a variável menu(com o menu de opções para o usuário.)
    if opcao == "D":
        os.system('cls')
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0: #Se o valor for maior que zero, será atribuido ao saldo.
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n' #Será acrescetado a informação do depósito à variável extrato.
        else: #Caso o usuário digite um valor negativo ou letras.
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 'S':
        os.system('cls')
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo #Caso o valor seja maior que o saldo.
        excedeu_limite = valor > limite #Caso o valor seja maior que o limite.
        excedeu_saques = numero_saques >= limite_saques #Caso o valor seja maior que o número de saques.
        if excedeu_saldo:
            os.system('cls')
            print('Você não tem saldo suficiente!')
        elif excedeu_limite:
            os.system('cls')
            print('Você excedeu o valor do limite de saque.')
        elif excedeu_saques:
            os.system('cls')
            print('Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor:.2f}\n'
            numero_saques += 1
        else:
            os.system('cls')
            print('O valor informado é inválido.')
    
    elif opcao == 'E':
        os.system('cls')
        print('Extrato\n')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R${saldo:.2f}')
        print('----------')
    
    elif opcao == 'Q':
        break
print('Conta fechada, volte sempre.')