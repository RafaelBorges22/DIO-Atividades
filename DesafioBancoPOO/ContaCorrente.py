from Conta import Conta
from Saque import Saque 

class ContaCorrente(Conta):
    def __init__(self, agencia, numero, cliente, historico, limite=500, limite_saques=3):
        super().__init__(agencia, numero, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([
            transacao for transacao in self.historico.transacoes
            if transacao["tipo"] == Saque.__name__
        ])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques 

        if excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")
            return False
        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques diários atingido.")
            return False
        else:
            return super().sacar(valor) 

    def __str__(self):
        return f"""\
        Agência: {self.agencia}
        C/C: {self.numero}
        Titular: {self.cliente.nome}
        """