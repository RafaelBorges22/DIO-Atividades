def menu():
    menu_opcoes = [
        "1. Depositar Dinheiro",
        "2. Consultar saldo",
        "3. Sacar Dinheiro",
        "4. Cadastrar Usuário",
        "5. Cadastrar Conta Bancária",
        "6. Listar Contas",
        "Q. Sair do sistema"
    ]
    print("\n================= MENU =================\n")
    print("Bem-vindo ao Banco do Rafael!")
    print("\n".join(menu_opcoes))
    return input("\nEscolha uma opção: ").upper()

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("Operação falhou! O valor informado é inválido. Digite apenas números.")
        return saldo, extrato

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("\nOperação falhou! O valor do depósito deve ser positivo.")
    
    return saldo, extrato

def consultar_saldo(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def sacar(saldo, extrato, limite, numero_saques, limite_saques, /):
    if numero_saques >= limite_saques:
        print("\nOperação falhou! Número máximo de saques diários atingido.")
        return saldo, extrato, numero_saques

    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("Operação falhou! O valor informado é inválido. Digite apenas números. \n")
        return saldo, extrato, numero_saques
        
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")

    return saldo, extrato, numero_saques

def encontrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuario):
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0, "extrato": [], "limite": 500, "numero_saques": 0, "limite_saques": 3}

def cadastrar_usuario(usuarios, contas):
    cpf = input("Informe o CPF (somente números): ")
    
    if encontrar_usuario(cpf, usuarios):
        print("\nERRO: Já existe um usuário com este CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    
    print("\nInforme o endereço:")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (sigla): ")
    
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    }

    AGENCIA = "0001"
    numero_conta = len(contas) + 1
    nova_conta = criar_conta(AGENCIA, numero_conta, novo_usuario)
    
    usuarios.append(novo_usuario)
    contas.append(nova_conta)
    
    print("\nUsuário e conta criados com sucesso!")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Conta: {AGENCIA}-{numero_conta}")
    print(f"Endereço: {novo_usuario['endereco']}")


def cadastrar_nova_conta(usuarios, contas):
    cpf = input("Informe o CPF do usuário para vincular a nova conta: ")
    usuario_encontrado = encontrar_usuario(cpf, usuarios)

    if usuario_encontrado:
        AGENCIA = "0001"
        numero_conta = len(contas) + 1
        nova_conta = criar_conta(AGENCIA, numero_conta, usuario_encontrado)
        contas.append(nova_conta)
        print(f"\nNova conta {AGENCIA}-{numero_conta} criada para o usuário {usuario_encontrado['nome']}.")
    else:
        print("\nUsuário não encontrado. Cadastre o usuário primeiro.")

def listar_contas(contas):
    for conta in contas:
        usuario = conta["usuario"]
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {usuario['nome']}")

def main():
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao in ("1", "2", "3"):
            if not contas:
                print("\nNenhuma conta cadastrada. Cadastre um usuário e conta primeiro.")
                continue

            conta = contas[0]
            saldo = conta["saldo"]
            extrato = conta["extrato"]
            limite = conta["limite"]
            numero_saques = conta["numero_saques"]
            limite_saques = conta["limite_saques"]

            if opcao == "1":
                saldo, extrato = depositar(saldo, extrato)
            elif opcao == "2":
                consultar_saldo(saldo, extrato)
            elif opcao == "3":
                saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, limite_saques)
            
            conta["saldo"] = saldo
            conta["extrato"] = extrato
            conta["numero_saques"] = numero_saques

        elif opcao == "4":
            cadastrar_usuario(usuarios, contas)

        elif opcao == "5":
            cadastrar_nova_conta(usuarios, contas)
        
        elif opcao == "6":
            if not contas:
                print("\nNenhuma conta cadastrada.")
            else:
                listar_contas(contas)
        
        elif opcao == "Q":
            print("\nObrigado por usar nosso sistema bancário. Até logo!")
            break
        
        else:
            print("\nOperação inválida, por favor selecione novamente a opção desejada.")

if __name__ == "__main__":
    main()