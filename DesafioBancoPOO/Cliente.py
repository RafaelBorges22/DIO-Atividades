class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao): 
        transacao.registrar(conta) 
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Endereco:
    def __init__(self, logradouro, numero, bairro, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro} - {self.cidade}/{self.estado}"