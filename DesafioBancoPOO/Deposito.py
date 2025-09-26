from Transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor 

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_trasacao = conta.depositar(self.valor) 
        if sucesso_trasacao:
            conta.historico.adicionar_transacao(self)