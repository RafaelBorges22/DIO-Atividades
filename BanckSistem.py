menu = [
    "1. Depositar Dinheiro",
    "2. Consultar saldo",
    "3. Sacar Dinheiro",
    "Q. Sair do sistema"
]

balance = 0
limit = 500
extract = []
number_withdrawal = 0
LIMIT_WITHDRAWAL = 3

while True:
    print("\n================= MENU ================= \n")
    print("Bem-vindo ao Banco do Rafael! \n")
    option = input("\nEscolha uma opção aí meu cliente: \n" + "\n".join(menu) + "\n Opção escolhida: ").upper()

    if option == "1":
        value = float(input("Informe o valor do depósito: "))

        if value > 0:
            balance += value
            extract.append(f"Depósito: R$ {value:.2f}")
            print(f"Depósito de R$ {value:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")


    elif option == "2":
        print("\n================ EXTRATO ================")
        if not extract:
            print("Não foram realizadas movimentações.")
        else:
            for item in extract:
                print(item)
        print(f"\nSaldo: R$ {balance:.2f}")
        print("=========================================")

    elif option == "3":
        if number_withdrawal >= LIMIT_WITHDRAWAL:
            print("Operação falhou! Número máximo de saques diários atingido.")
            continue

        value = float(input("Informe o valor do saque: "))

        if value > balance:
            print("Operação falhou! Saldo insuficiente.")
        elif value > limit:
            print("Operação falhou! O valor do saque excede o limite.")
        elif value <= 0:
            print("Operação falhou! O valor informado é inválido.")
        else:
            balance -= value
            extract.append(f"Saque: R$ {value:.2f}")
            number_withdrawal += 1
            print(f"Saque de R$ {value:.2f} realizado com sucesso.")

    elif option == "Q":
        print("Obrigado por usar nosso sistema bancário. Até logo!")
        break





