from Models import *


class DaoCategoria:
    @classmethod
    def limpar(cls):
        with open("categoria.txt", "w") as arq:
            arq.writelines("")
    @classmethod
    def salvar(cls, categoria):
        with open("categoria.txt", "a") as arq:
            arq.writelines(categoria + ";" + "\n")
    @classmethod
    def ler(cls):
        with open("categoria.txt", "r") as arq:
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria ))
        cls.categoria = list(map(lambda x: x.replace(';', ''), cls.categoria ))
        lista_categoria = []
        for cat in cls.categoria:
            lista_categoria.append(Categoria(cat))
        return lista_categoria

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open("venda.txt", "a") as arq:
            arq.writelines(venda.produto.nome + ";" + str(venda.produto.preco) + ";"  + venda.produto.categoria + ";" +
                           venda.comprador + ";" + venda.vendedor + ";" + str(venda.quantidade) + ";" +
                           venda.data + ";" + "\n")
    @classmethod
    def ler(cls):
        with open("venda.txt", "r") as arq:
            cls.venda = arq.readlines()
            cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda ))
            lista_venda = []
            for ven in cls.venda:
                item = ven.split(sep=";")
                lista_venda.append(Venda(Produto(item[0], item[1], item[2]), item[3], item[4], item[5], item[6]))
            return lista_venda
        
class DaoEstoque:
    @classmethod
    def limpar(cls):
        with open("estoque.txt", "w") as arq:
            arq.writelines("")    
    @classmethod
    def salvar(cls, produto : Produto , quantidade):
        with open("estoque.txt", "a") as arq:
            arq.writelines(produto.nome + ";" + str(produto.preco) + ";"  + produto.categoria + ";" +
                           str(quantidade) + ";" + "\n")
    @classmethod
    def ler(cls):
        with open("estoque.txt", "r") as arq:
            cls.estoque = arq.readlines()
            cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque ))
            lista_estoque = []
            for est in cls.estoque:
                item = est.split(sep=";")
                lista_estoque.append(Estoque(Produto(item[0], item[1], item[2]), item[3]))
            return lista_estoque

class DaoFornecedor:
    @classmethod
    def limpar(cls):
        with open("fornecedor.txt", "w") as arq:
            arq.writelines("")    
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open("fornecedor.txt", "a") as arq:
            arq.writelines(fornecedor.nome + ";" + str(fornecedor.cnpj) + ";"  + fornecedor.telefone + ";" +
                           fornecedor.email + ";" + str(fornecedor.categoria) + ";" + "\n")
    @classmethod
    def ler(cls):
        with open("fornecedor.txt", "r") as arq:
            cls.fornecedor = arq.readlines()
            cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor ))
            lista_fornecedor = []
            for fornec in cls.fornecedor:
                item = fornec.split(sep=";")
                lista_fornecedor.append(Fornecedor(item[0], item[1], item[2], item[3], item[4]))
            return lista_fornecedor   

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoa.txt", "a") as arq:
            arq.writelines(pessoa.nome + ";" + str(pessoa.idade) + ";"  + pessoa.cpf + ";" +
                           pessoa.telefone + ";" + str(pessoa.email) + ";"  + pessoa.endereco + ";" + "\n")
    @classmethod
    def ler(cls):
        with open("pessoa.txt", "r") as arq:
            cls.pessoa = arq.readlines()
            cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa ))
            lista_pessoa = []
            for pess in cls.pessoa:
                item = pess.split(sep=";")
                lista_pessoa.append(Pessoa(item[0], item[1], item[2], item[3], item[4], item[5]))
            return lista_pessoa

class DaoFuncionario:
    @classmethod
    def limpar(cls):
        with open("funcionario.txt", "w") as arq:
            arq.writelines("")    
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open("funcionario.txt", "a") as arq:
            arq.writelines(funcionario.clt + ";" + funcionario.salario + ";"  + funcionario.nome + ";" +
                           funcionario.idade + ";" + funcionario.cpf + ";"  + funcionario.telefone + ";" + 
                           funcionario.email + ";" + funcionario.endereco + "\n")
    @classmethod
    def ler(cls):
        with open("funcionario.txt", "r") as arq:
            cls.funcionario = arq.readlines()
            cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario ))
            lista_funcionario = []
            for func in cls.funcionario:
                item = func.split(sep=";")
                lista_funcionario.append(Funcionario(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]))
            return lista_funcionario

class DaoCliente:
    @classmethod
    def limpar(cls):
        with open("cliente.txt", "w") as arq:
            arq.writelines("")      
    @classmethod
    def salvar(cls, cliente: Cliente):
        with open("cliente.txt", "a") as arq:
            arq.writelines(cliente.nome + ";" + str(cliente.idade) + ";"  + cliente.cpf + ";" +
                           cliente.telefone + ";" + str(cliente.email) + ";"  + cliente.endereco + ";" + "\n")
    @classmethod
    def ler(cls):
        with open("cliente.txt", "r") as arq:
            cls.cliente = arq.readlines()
            cls.cliente = list(map(lambda x: x.replace('\n', ''), cls.cliente ))
            lista_cliente = []
            for cli in cls.cliente:
                item = cli.split(sep=";")
                lista_cliente.append(Cliente(item[0], item[1], item[2], item[3], item[4], item[5]))
            return lista_cliente
