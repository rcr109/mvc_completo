import os.path

import Controller
from Models import Produto


def gera_arquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")

gera_arquivos('categoria.txt','cliente.txt','estoque.txt','fornecedor.txt','funcionario.txt','venda.txt')

if __name__ == "__main__":

#Menu PRINCIPAL      
    while True:
        print('================================================================================')
        print('=                          SELECIONE UMA DAS OPCOES                            =')
        print('================================================================================')
        print('=  1 - CATEGORIAS                                                              =')
        print('=  2 - ESTOQUES                                                                =')        
        print('=  3 - FORNECEDORES                                                            =')        
        print('=  4 - CLIENTES                                                                =')        
        print('=  5 - FUNCIONARIOS                                                            =')  
        print('=  6 - VENDAS                                                                  =')              
        print('=  7 - PRODUTOS MAIS VENDIDOS                                                  =')        
        print('=  8 - SAIR                                                                    =')        
        print('================================================================================')
        opcao = int(input('DIGITE: '))

#Menu CATEGORIAS 
        if opcao == 1:
            while True:
                print('================================================================================')
                print('=                 SELECIONE A OPERAÇÃO NAS CATEGORIAS                          =')
                print('================================================================================')
                print('=  1 - INCLUIR                                                                 =')
                print('=  2 - EDITAR                                                                  =')        
                print('=  3 - EXCLUIR                                                                 =')        
                print('=  4 - CONSULTAR                                                               =')        
                print('=  5 - SAIR                                                                    =')        
                print('================================================================================')
                opcao_categ = int(input('DIGITE: '))       
                if opcao_categ == 1:
                    nome = input('Digite um nome para a categoria: ')
                    if nome != '' and nome != ' ':
                        Controller.ControllerCategoria.cad_categoria('View', nome)
                    else:
                        print("Digite um nome válido para a categoria.")
                if opcao_categ == 2:
                    nome_antes = input("Digite o nome da categoria que deseja alterar: ")
                    nom_depois = input("Digite o novo nome para a categoria: ")
                    if nome_antes != '' and nom_depois != '':
                        Controller.ControllerCategoria.alt_categoria('View', nome_antes, nom_depois)
                    else:
                        print("Digite nomes válidos para as categorias.")
                if opcao_categ == 3:
                    nome = input("Digite o nome da categoria que deseja excluir: ")
                    if nome != '':
                        Controller.ControllerCategoria.del_categoria('View', nome)
                    else:
                        print("Digite um nome válido para a categoria.")
                if opcao_categ == 4:
                    Controller.ControllerCategoria.exi_categorias('')     
                if opcao_categ == 5:
                    break

#Menu ESTOQUES 
        if opcao == 2:
            while True:
                print('================================================================================')
                print('=                 SELECIONE A OPERAÇÃO NAS ESTOQUES                            =') #=======================================
                print('================================================================================')
                print('=  1 - INCLUIR PRODUTO NO ESTOQUE                                              =')
                print('=  2 - MODIFICAR PRODUTO NO ESTOQUE                                            =')        
                print('=  3 - EXCLUIR PRODUTO DO ESTOQUE                                              =')        
                print('=  4 - CONSULTAR ESTOQUE                                                       =')        
                print('=  5 - SAIR                                                                    =')        
                print('================================================================================')
                opcao_est = int(input('DIGITE: ')) 
                if opcao_est == 1:
                    nome = input("Digite nome do produto: ")
                    preco = input("Digite o preco do produto: ")
                    categoria = input("Digite a categoria do produto: ")
                    quantidade = input("Digite a quantidade:")
                    if nome != '' and preco != '' and categoria != '' and quantidade!= '':
                        Controller.ControllerEstoque.cad_produto('View', nome, preco, categoria, quantidade)
                    else:
                        print("É necessário digitar todos os dados.")
                if opcao_est == 2:
                    nome = input("Digite o nome do produto que deseja alterar: ")
                    nome_novo = input("Digite o novo nome para o produto: ")                    
                    preco = input("Digite o novo preço para o produto: ")
                    categoria = input("Digite a nova categoria para o produto: ")
                    quantidade = input("Digite a nova quantidade: ")
                    if nome != '' and nome_novo != '' and preco != '' and categoria != '' and quantidade != '':
                        Controller.ControllerEstoque.alt_produto('', nome, nome_novo, preco, categoria, quantidade)
                    else:
                        print("É necessário digitar todos os dados.")
                if opcao_est == 3:
                    nome = input("Digite o nome do produto que deseja excluir: ")
                    if nome != '':
                        Controller.ControllerEstoque.del_produto('', nome)
                    else:
                        print("Digite um nome válido para o produto.")
                if opcao_est == 4:
                    Controller.ControllerEstoque.exi_produtos('')     
                if opcao_est == 5:
                    break

#Menu FORNECEDORES  
        if opcao == 3:
            while True:
                print('================================================================================')
                print('=                 SELECIONE A OPERAÇÃO NOS FORNECEDORES                        =')
                print('================================================================================')
                print('=  1 - INCLUIR                                                                 =')
                print('=  2 - EDITAR                                                                  =')        
                print('=  3 - EXCLUIR                                                                 =')        
                print('=  4 - CONSULTAR                                                               =')        
                print('=  5 - SAIR                                                                    =')        
                print('================================================================================')
                opcao_fornec = int(input('DIGITE: '))            
                if opcao_fornec == 1:
                    nome = input("Digite um nome para o fornecedor: ")
                    cnpj = input("Digite um CNPJ para o fornecedor: ")
                    telefone = input("Digite um telefone para o fornecedor: ")
                    email = input("Digite um e-mail para o fornecedor: ")
                    categoria = input("Digite uma categoria para o fornecedor: ")
                    if nome != '' and cnpj != '' and telefone != '' and email != '' and categoria != '':
                        Controller.ControllerFornecedor.cad_fornecedor('View', nome, cnpj, telefone, email, categoria)
                    else:
                       print("É necessário digitar todos os dados.")
                if opcao_fornec == 2:
                    cnpj = input("Digite o CNPJ do fornecedor que deseja alterar: ")                    
                    nome = input("Digite um nome para o fornecedor: ")
                    telefone = input("Digite um telefone para o fornecedor: ")
                    email = input("Digite um e-mail para o fornecedor: ")
                    categoria = input("Digite uma categoria para o fornecedor: ")                    
                    if nome != '' and cnpj != '' and telefone != '' and email != '' and categoria != '':
                        Controller.ControllerFornecedor.alt_fornecedor('View',nome, cnpj, telefone, email, categoria)
                    else:
                        print("É necessário digitar todos os dados.")
                if opcao_fornec == 3:
                    cnpj = input("Digite o CNPJ do fornecedor que deseja excluir: ")
                    if cnpj != '':
                        Controller.ControllerFornecedor.del_fornecedor('View', cnpj)
                    else:
                        print("Digite um CNPJ válido para o fornecedor.")
                if opcao_fornec == 4:
                    Controller.ControllerFornecedor.exi_fornecedor('View')
                if opcao_fornec == 5:
                    break

#Menu CLIENTES  
        if opcao == 4:
            while True:
                print('================================================================================')
                print('=                 SELECIONE A OPERAÇÃO NOS CLIENTES                            =')
                print('================================================================================')
                print('=  1 - INCLUIR                                                                 =')
                print('=  2 - EDITAR                                                                  =')        
                print('=  3 - EXCLUIR                                                                 =')        
                print('=  4 - CONSULTAR                                                               =')        
                print('=  5 - SAIR                                                                    =')        
                print('================================================================================')
                opcao_cli = int(input('DIGITE: '))        
                if opcao_cli == 1:
                    nome = input("Digite um nome para o cliente: ")
                    idade = input("Digite a idade do cliente: ")
                    cpf = input("Digite um CPF para o cliente: ")
                    telefone = input("Digite um telefone para o cliente: ")
                    email = input("Digite um e-mail para o cliente: ")
                    endereco = input("Digite uma endereco para o cliente: ")
                    if nome != '' and cpf != '' and telefone != '' and email != '' and endereco != '' and idade != '':
                        Controller.ControllerCliente.cad_cliente('View',nome, idade, cpf, telefone, email, endereco)
                    else:
                       print("É necessário digitar todos os dados.")
                if opcao_cli == 2:
                    cpf = input("Digite o CPF do cliente que deseja alterar: ")                    
                    nome = input("Digite um nome para o cliente: ")
                    idade = input("Digite a idade do cliente: ")                    
                    telefone = input("Digite um telefone para o cliente: ")
                    email = input("Digite um e-mail para o cliente: ")
                    endereco = input("Digite uma endereco para o cliente: ")                    
                    if nome != '' and cpf != '' and telefone != '' and email != '' and endereco != '' and idade != '':
                        Controller.ControllerCliente.alt_cliente('View',nome, idade, cpf, telefone, email, endereco)
                    else:
                        print("É necessário digitar todos os dados.")
                if opcao_cli == 3:
                    cpf = input("Digite o CPF do cliente que deseja excluir: ")
                    if cpf != '':
                        Controller.ControllerCliente.del_cliente('View', cpf)
                    else:
                        print("Digite um CPF válido para o cliente.")
                if opcao_cli == 4:
                    Controller.ControllerCliente.exi_clientes('View')
                if opcao_cli == 5:
                    break

#Menu FUNCIONÁRIOS                    
        if opcao == 5:
            while True:
                print('================================================================================')
                print('=                 SELECIONE A OPERAÇÃO NOS FUNCIONÁRIOS                        =')
                print('================================================================================')
                print('=  1 - INCLUIR                                                                 =')
                print('=  2 - EDITAR                                                                  =')        
                print('=  3 - EXCLUIR                                                                 =')        
                print('=  4 - CONSULTAR                                                               =')        
                print('=  5 - SAIR                                                                    =')        
                print('================================================================================')
                opcao_func = int(input('DIGITE: '))            

                if opcao_func == 1:
                    clt = input("Digite um número de CLT para o funcionário: ")
                    salario = input("Digite um salário: ")
                    nome = input("Digite um nome para o funcionário: ")
                    idade = input("Digite a idade do funcionário: ")
                    cpf = input("Digite um CPF para o funcionário: ")
                    telefone = input("Digite um telefone para o funcionário: ")
                    email = input("Digite um e-mail para o funcionário: ")
                    endereco = input("Digite uma endereco para o funcionário: ")
                    if nome != '' and cpf != '' and telefone != '' and email != '' and endereco != '' and idade != '' and clt != '' and str(salario) != '':
                        Controller.ControllerFuncionario.cad_funcionario('View', clt, salario, nome, idade, cpf, telefone, email, endereco)
                    else:
                       print("É necessário digitar todos os dados.")
                if opcao_func == 2:
                    cpf = input("Digite o CPF do funcionario que deseja alterar: ")    
                    clt = input("Digite um número de CLT para o funcionário: ")
                    salario = input("Digite um salário: ")                                    
                    nome = input("Digite um nome para o funcionário: ")
                    idade = input("Digite a idade do funcionário: ")                    
                    telefone = input("Digite um telefone para o funcionário: ")
                    email = input("Digite um e-mail para o funcionário: ")
                    endereco = input("Digite uma endereco para o funcionário: ")                    
                    if nome != '' and cpf != '' and telefone != '' and email != '' and endereco != '' and idade != '' and clt != '' and str(salario) != '':
                        Controller.ControllerFuncionario.alt_funcionario('View', clt, salario, nome, idade, cpf, telefone, email, endereco)
                    else:
                        print("É necessário digitar todos os dados.")
                if opcao_func == 3:
                    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
                    if cpf != '':
                        Controller.ControllerFuncionario.del_funcionario('View', cpf)
                    else:
                        print("Digite um CPF válido para o funcionário.")
                if opcao_func == 4:
                    Controller.ControllerFuncionario.exi_funcionarios('View')
                if opcao_func == 5:
                    break              

#Menu VENDAS
        if opcao == 6:
            while True:
                print('================================================================================')
                print('=                 SELECIONE A OPERAÇÃO EM VENDAS                               =')
                print('================================================================================')
                print('=  1 - REGISTRAR VENDA                                                         =')
                print('=  2 - EXIBIR VENDAS                                                           =')        
                print('=  3 - SAIR                                                                    =')        
                print('================================================================================')
                opcao_vendas = int(input('DIGITE: '))            
                if opcao_vendas == 1:
                    nome = input("Digite nome do produto: ")
                    preco = input("Digite o preco do produto: ")
                    categoria = input("Digite a categoria do produto: ")
                    quantidade_prod = '0'
                    quantidade = input("Digite a quantidade vendida: ")
                    comprador = input("Digite o nome do comprador: ")
                    vendedor = input("Digite o nome do vendedor: ")
                    if nome != '' and preco != '' and categoria != '' and quantidade!= '' and comprador != '' and vendedor != '':
                        Controller.ControllerVenda.cad_venda('', Produto(nome, preco, categoria), comprador, vendedor, quantidade)
                    else:
                        print("É necessário digitar todos os dados.")
                if opcao_vendas == 2:
                    inicio = input("Digite a data de início do filtro (dd/mm/aaaa): ")
                    fim = input("Digite a data de fim do filtro (dd/mm/aaaa): ")
                    Controller.ControllerVenda.exi_vendas('', inicio, fim)
                if opcao_vendas == 3:
                    break

#Menu PRODUTOS MAIS VENDIDOS
        if opcao == 7:
            Controller.ControllerVenda.rel_vendas('')
#SAIR  
        if opcao == 8:
            break