from Historico import Historico

class Conta():
    def __init__(self, agencia, numero, cliente, historico):
        self._agencia = agencia
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._historico = historico 

    @classmethod
    def criar_conta(cls, agencia, numero, cliente, historico):
        return cls(agencia, numero, cliente, historico)

    @property
    def saldo(self):
        return self._saldo

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self): 
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
            return True
        else:
            print("\nOperação falhou! O valor informado é inválido.")
            return False

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self._saldo -= valor
            return True 
        else:
            print("\nOperação falhou! O valor informado é inválido.")
        return False
        



