from Cliente import Cliente, Endereco 

class PessoaFisica(Cliente): 
    def __init__(self, nome, cpf, data_nascimento, endereco): 
        super().__init__(nome, endereco) 
        self.cpf = cpf
        self.data_nascimento = data_nascimento