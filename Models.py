from datetime import datetime


class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, produto: Produto, comprador, vendedor, quantidade, data = datetime.now().strftime("%d/%m/%Y")):
        self.produto = produto
        self.comprador = comprador
        self.vendedor = vendedor
        self.quantidade = quantidade        
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, email, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, idade, cpf, telefone, email, endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, clt, salario, nome, idade, cpf, telefone, email, endereco):
        self.clt = clt
        self.salario = salario
        super(Funcionario, self).__init__(nome, idade, cpf, telefone, email, endereco)

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, telefone, email, endereco):
        super(Cliente, self).__init__(nome, idade, cpf, telefone, email, endereco)