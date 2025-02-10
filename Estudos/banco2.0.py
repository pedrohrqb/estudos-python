import textwrap


def menu():
    menu = """\n
    =================== MENU ==================

    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [NC]\tNova Conta
    [LC]\tListar Contas
    [NU]\tNovo Usuário
    [Q]\tSair
    => """
    return input(textwrap.dedent(menu)).upper()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')
    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limites_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limites_saques

    if excedeu_saldo:
        print('\n@@@ Operação falhou! Você não tem saldo suficiente. @@@')
    elif excedeu_limite:
        print('\n@@@ Operação falhou! O valor do saque excedeu o limite. @@@')
    elif excedeu_saques:
        print('\n@@@ Operação falhou! Número máximo de saques excedido. @@@')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')
    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
        
    return saldo, extrato
        
def exibir_extrato(saldo, /, *, extrato):
    print('\n================= EXTRATO ===================')       
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('=====================================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)     

    if usuario:
        print('\n@@@ Já existe usuário com esse CPF! @@@')
        return
    
    nome = str(input('Informe o nome completo: ')).upper()
    data_nascimento = int(input('Informe a data de nascimento (dd-mm-aaaa): '))
    endereco = str(input('informe o endereço (logradouro, nro - bairro - cidade/sigla estado): '))
    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco': endereco})

    print('=== Usuário criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input('Informe o CPF do usuário: '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    
    print('\n@@@ Usuário não encontrato, fluxo de criação de conta encerrado! @@@')

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'D':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 'S':
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'NU':
            criar_usuario(usuarios)

        elif opcao == 'NC':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                conta.append(conta)
        
        elif opcao == 'LC':
            listar_contas(contas)

        elif opcao == 'Q':
            break

        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')

main()            