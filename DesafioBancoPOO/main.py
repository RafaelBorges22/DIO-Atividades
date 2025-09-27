from PessoaFisica import PessoaFisica, Endereco
from ContaCorrente import ContaCorrente
from Historico import Historico
from Deposito import Deposito
from Saque import Saque

clientes = []
contas = []

def criar_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nasc = input("Data de nascimento (dd/mm/aaaa): ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    endereco = Endereco(logradouro, numero, bairro, cidade, estado)
    cliente = PessoaFisica(nome, cpf, data_nasc, endereco)
    clientes.append(cliente)
    print("\n✅ Cliente criado com sucesso!")

def criar_conta():
    if not clientes:
        print("\n⚠️ Nenhum cliente cadastrado ainda.")
        return
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if cliente:
        numero = len(contas) + 1
        conta = ContaCorrente("0001", numero, cliente, Historico())
        cliente.adicionar_conta(conta)
        contas.append(conta)
        print("\n✅ Conta criada com sucesso!")
    else:
        print("\n⚠️ Cliente não encontrado.")

def depositar():
    numero = int(input("Número da conta: "))
    conta = next((c for c in contas if c.numero == numero), None)
    if conta:
        valor = float(input("Valor do depósito: "))
        transacao = Deposito(valor)
        conta.cliente.realizar_transacao(conta, transacao)
    else:
        print("\n⚠️ Conta não encontrada.")

def sacar():
    numero = int(input("Número da conta: "))
    conta = next((c for c in contas if c.numero == numero), None)
    if conta:
        valor = float(input("Valor do saque: "))
        transacao = Saque(valor)
        conta.cliente.realizar_transacao(conta, transacao)
    else:
        print("\n⚠️ Conta não encontrada.")

def extrato():
    numero = int(input("Número da conta: "))
    conta = next((c for c in contas if c.numero == numero), None)
    if conta:
        print("\n====== Extrato ======")
        if not conta.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for t in conta.historico.transacoes:
                print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")
        print("=====================")
    else:
        print("\n⚠️ Conta não encontrada.")

def listar_contas():
    if not contas:
        print("\n⚠️ Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(conta)

def main():
    while True:
        print("\n===== MENU =====")
        print("1 - Criar cliente")
        print("2 - Criar conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Extrato")
        print("6 - Listar contas")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cliente()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            depositar()
        elif opcao == "4":
            sacar()
        elif opcao == "5":
            extrato()
        elif opcao == "6":
            listar_contas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("\n⚠️ Opção inválida!")

if __name__ == "__main__":
    main()
