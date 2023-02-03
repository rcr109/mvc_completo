from datetime import datetime

from DAO import (DaoCategoria, DaoCliente, DaoEstoque, DaoFornecedor,
                 DaoFuncionario, DaoVenda)
from Models import (Categoria, Cliente, Estoque, Fornecedor, Funcionario,
                    Produto, Venda)


class ControllerCategoria:
    def cad_categoria(self, novaCategoria):
        all_categs = DaoCategoria.ler()
        ja_existe_cat = list(filter(lambda x: x.categoria == novaCategoria, all_categs))
        if ja_existe_cat:
            print(f'A categoria {novaCategoria} já existe.')
        else:
            DaoCategoria.salvar(novaCategoria)
            print(f'Categoria {novaCategoria} cadastrada com sucesso.')
    def del_categoria(self, categoria_remover):
        all_categs = DaoCategoria.ler()        
        ja_existe_cat = list(filter(lambda x: x.categoria == categoria_remover, all_categs))
        if not ja_existe_cat:
            print(f'A categoria {categoria_remover} não existe.')
        else:
            for i in range(len(all_categs)):
                if all_categs[i].categoria == categoria_remover:
                    del all_categs[i]
                    break
            print(f'A categoria {categoria_remover} foi excluída com sucesso.')
            DaoCategoria.limpar()
            for i in all_categs:
                DaoCategoria.salvar(i.categoria)
            all_estoques = DaoEstoque.ler()
            new_all_estoques = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, 'SEM CATEGORIA'),x.quantidade) if (x.produto.categoria == categoria_remover) else(x), all_estoques))
            DaoEstoque.limpar()
            for est in new_all_estoques:
                DaoEstoque.salvar(est.produto, est.quantidade)
            print(f'Os itens de estoque foram atualizados com sucesso.')
    def alt_categoria(self, categoria_antes, categoria_depois):
        all_categs = DaoCategoria.ler()        
        ja_existe_cat = list(filter(lambda x: x.categoria == categoria_antes, all_categs))        
        if ja_existe_cat:
            cat1 = list(filter(lambda x: x.categoria == categoria_depois, all_categs))  
            if cat1:
                print(f'A categoria {categoria_depois} já existe.')
            else:
                categoria_nova = list(map(lambda x: Categoria(categoria_depois) if (x.categoria == categoria_antes) else (x), all_categs)) 
                DaoCategoria.limpar()
                for i in range(len(categoria_nova)):
                    DaoCategoria.salvar(categoria_nova[i].categoria)
                    print(categoria_nova[i].categoria)
                print(f'A categoria {categoria_antes} foi alterada para {categoria_depois}.')
                all_estoques = DaoEstoque.ler()
                new_all_estoques = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, categoria_depois),x.quantidade) if (x.produto.categoria == categoria_antes) else(x), all_estoques))
                DaoEstoque.limpar()
                for est in new_all_estoques:
                    DaoEstoque.salvar(est.produto, est.quantidade)
                print(f'Os itens de estoque foram atualizados com sucesso.')
        else:
            print(f'A categoria {categoria_antes} não existe.')
    def exi_categorias(self):
        categorias = DaoCategoria.ler() 
        if len(categorias) == 0:
            print('Não existem categorias cadastradas.')
        else:
            for x in categorias:
                print(f'Descrição: {x.categoria.upper()}')

class ControllerEstoque:
    def cad_produto(self, nome, preco, categoria, quantidade):
        prod = DaoEstoque.ler()
        cate = DaoCategoria.ler()
        cate_exist = list(filter(lambda x: x.categoria == categoria, cate))
        prod_exist = list(filter(lambda x: x.produto.nome == nome, prod))
        if len(cate_exist) > 0:
            if len(prod_exist) == 0:
                produto = Produto (nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print(f'Produto {nome} cadastrado com sucesso.')    
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria inexistente.')   
    def del_produto(self, nome):
        prod = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, prod))
        if len(est) > 0:
            prod = list(filter(lambda x: x.produto.nome != nome, prod))
            for i in range(len(prod)):
                if prod[i].produto.nome == nome:
                    del prod[i]
                    break
            print(f'O produto {nome} foi excluído.')
        else:
            print(f'O produto {nome} não existe no estoque.') 
        DaoEstoque.limpar()  
        for i in range(len(prod)):
            DaoEstoque.salvar( Produto(prod[i].produto.nome,prod[i].produto.preco,prod[i].produto.categoria), prod[i].quantidade)         
    def alt_produto(self, produto_antes, produto_depois, novo_preco, nova_categoria, nova_quantidade):
        ests = DaoEstoque.ler()   
        cats = DaoCategoria.ler()     
        cat_exists = list(filter(lambda x: x.categoria == nova_categoria, cats))  
        if len(cat_exists) > 0:
            prod_exists = list(filter(lambda x: x.produto.nome == produto_antes, ests))
            if not prod_exists:
                print(f'O produto {produto_antes} não existe.')
            else:
                prod_jah_existe = list(filter(lambda x: x.produto.nome == produto_depois and x.produto.nome != produto_antes, ests))
                if prod_jah_existe:
                    print(f"O produto {produto_depois} já existe no cadastro.")
                    return
                novos_ests = list(map(lambda x: Estoque(Produto(produto_depois, novo_preco, nova_categoria), nova_quantidade) if (x.produto.nome == produto_antes) else (x), ests))
                #TODO: ALTERAR PRODUTO NO ESTOQUE AO ALTERAR EM PRODUTOS
                DaoEstoque.limpar()
                for i in range(len(novos_ests)):
                    DaoEstoque.salvar(Produto(novos_ests[i].produto.nome, novos_ests[i].produto.preco, novos_ests[i].produto.categoria), novos_ests[i].quantidade)
                print(f'A produto {produto_antes} foi alterado para {produto_depois}.')
        else:
            print(f'A categoria {nova_categoria} não existe.')    
    def exi_produtos(self):
        produtos = DaoEstoque.ler()
        if not produtos:
            print("Não existem produtos cadastrados no estoque.")
        else:
            for i in range(len(produtos)):
                print(f"Produto: {produtos[i].produto.nome.upper()}, Preço: {produtos[i].produto.preco}, Categoria: {produtos[i].produto.categoria.upper()}, Quantidade: {produtos[i].quantidade}")

class ControllerVenda:
    def cad_venda(self, produto: Produto, comprador, vendedor, quantidade):
        prod_all = DaoEstoque.ler()
        nova_venda = Venda(produto, comprador, vendedor, quantidade)
        prod_exists = list(filter(lambda x: produto.nome == x.produto.nome, prod_all))
        if prod_exists:
            if int(quantidade) <= int(prod_exists[0].quantidade):
                valor_compra = float(int(nova_venda.quantidade) * int(nova_venda.produto.preco))
                DaoVenda.salvar(nova_venda)
                prod_all = list(map(lambda x: Estoque(produto, (int(prod_exists[0].quantidade) - int(quantidade))) if (produto.nome == x.produto.nome) else (x), prod_all))
                DaoEstoque.limpar()
                for i in range(len(prod_all)):
                    DaoEstoque.salvar(prod_all[i].produto, prod_all[i].quantidade)
                print(f"Venda cadastrada com sucesso. Valor: R${valor_compra}")
                return valor_compra
            else:
                print(f"Não há quantidade suficiente em estoque. Existente: {prod_exists[0].quantidade}")
                return None
        else:
            print("Este produto não existe.")
            return None
    def exi_vendas(self, inicio, fim):
        vendas = DaoVenda.ler()
        data_inicio = datetime.strptime(inicio, '%d/%m/%Y')
        data_fim = datetime.strptime(fim, '%d/%m/%Y')

        vendas_selecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= data_inicio and datetime.strptime(x.data, '%d/%m/%Y') <= data_fim, vendas))
        if len(vendas_selecionadas) > 0:
            for i in range(len(vendas_selecionadas)):
                print(f'Comprador: {vendas_selecionadas[i].comprador.upper()}, Produto: {vendas_selecionadas[i].produto.nome.upper()}, Quantidade: {vendas_selecionadas[i].quantidade}, Preço: {vendas_selecionadas[i].produto.preco}, Data: {vendas_selecionadas[i].data}, Total: {str(int(vendas_selecionadas[i].quantidade) * float(vendas_selecionadas[i].produto.preco))}')
        else:
            print('Não existem vendas cadastradas.')
    def rel_vendas(self):
        allvendas = DaoVenda.ler()
        vendas = []
        for i in allvendas:
            #print(i.produto.nome)
            quantidade = i.quantidade
            nome = i.produto.nome
            tamanho = list(filter(lambda x: x['produto'] == i.produto.nome, vendas))
            if tamanho:
                vendas = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)} 
                                  if (x['produto'] == nome) 
                                  else(x), vendas))
            else:
                vendas.append({'produto': nome.upper(), 'quantidade' : int(quantidade)})
        ordenada = sorted(vendas, key=lambda k: k['quantidade'], reverse=True )    
        print('Produtos mais vendidos:')
        for item_rel in ordenada:
            print(f'{item_rel}')

class ControllerFornecedor:
    def cad_fornecedor(self, nome, cnpj, telefone, email, categoria):
        all_fornecs = DaoFornecedor.ler()
        all_categs = DaoCategoria.ler()
        ja_existe_fornec = list(filter(lambda x: x.cnpj == cnpj, all_fornecs))
        if not ja_existe_fornec:
            existe_categ = list(filter(lambda x: x.categoria == categoria, all_categs))
            if existe_categ:
                fornecedor = Fornecedor(nome, cnpj, telefone, email, categoria)
                DaoFornecedor.salvar(fornecedor)
                print(f'Fornecedor {nome} cadastrado com sucesso.')
                return fornecedor
            else:
                print(f'A categoria {categoria} nào existe.')
                return None
        else:
            print(f"Já existe um fornecedor com o CNPJ {cnpj} cadastrado.")
            return None
    def del_fornecedor(self, cnpj):
        all_fornecs = DaoFornecedor.ler()
        ja_existe_fornec = list(filter(lambda x: x.cnpj == cnpj, all_fornecs))
        if ja_existe_fornec:
            for i in range(len(all_fornecs)):
                if all_fornecs[i].cnpj == cnpj:
                    del all_fornecs[i]
                    DaoFornecedor.limpar()
                    for fornec in all_fornecs:
                        DaoFornecedor.salvar(fornec)
                    print(f'Fornecedor com CNPJ {cnpj} excluído com sucesso.')                        
                    break                    
        else:
            print(f"Não existe fornecedor cadastrado com o CNPJ {cnpj}.")
    def alt_fornecedor(self, nome_novo, cnpj, telefone_novo, email_novo, categoria_nova):
        all_fornecs = DaoFornecedor.ler()
        all_categs = DaoCategoria.ler()
        ja_existe_fornec = list(filter(lambda x: x.cnpj == cnpj, all_fornecs))
        if ja_existe_fornec:
            existe_categ = list(filter(lambda x: x.categoria == categoria_nova, all_categs))
            if existe_categ:
                fornecedor_editado = Fornecedor(nome_novo, cnpj, telefone_novo, email_novo, categoria_nova)
                all_fornecs = list(map(lambda x: fornecedor_editado if (x.cnpj == cnpj) else (x), all_fornecs))
                DaoFornecedor.limpar()                
                for i in all_fornecs:
                    DaoFornecedor.salvar(i)
                print(f"Fornecedor de CNPJ: {cnpj} editado com sucesso.")
                return fornecedor_editado
            else:
                print(f'A categoria {categoria_nova} não existe.')
                return None
        else:
            print(f'Não existe um fornecedor com o CNPJ {cnpj} cadastrado.')   
            return None 
    def exi_fornecedor(self):
        all_fornecs = DaoFornecedor.ler()
        if all_fornecs:
            for fornec in all_fornecs:
                print(f'FORNECEDOR: {fornec.nome.upper()}, CNPJ: {fornec.cnpj}, E-MAIL: {fornec.email}, CATEGORIA: {fornec.categoria}')
        else:
            print('Não existe nenhum forncedor cadastrado.')

class ControllerFuncionario:
    def cad_funcionario(self, clt, salario, nome, idade, cpf, telefone, email, endereco):
        all_funcs = DaoFuncionario.ler()
        ja_existe_func = list(filter(lambda x: x.cpf == cpf, all_funcs))
        if not ja_existe_func:
            funcionario_novo = Funcionario(clt, salario, nome, idade, cpf, telefone, email, endereco)
            DaoFuncionario.salvar(funcionario_novo)
            print(f'Funcionário de CPF: {cpf} cadastrado com sucesso')
            return funcionario_novo
        else:
            print(f'Já existe um funcionário cadastrado com o CPF: {cpf}.')
            return None      
    def del_funcionario(self, cpf):
        all_funcs = DaoFuncionario.ler()
        ja_existe_func = list(filter(lambda x: x.cpf == cpf, all_funcs))
        if ja_existe_func:
            for i in range(len(all_funcs)):
                if all_funcs[i].cpf == cpf:
                    del all_funcs[i]
                    break
            DaoFuncionario.limpar()
            for func in all_funcs:
                DaoFuncionario.salvar(func)
            print(f'O funcionário de CPF: {cpf} foi excluído.')
        else:
            print(f'Não existe um funcionário cadastrado com o CPF: {cpf}')
    def alt_funcionario(self, clt_nova, salario_novo, nome_novo, idade_nova, cpf, telefone_novo, email_novo, endereco_novo):
        all_funcs = DaoFuncionario.ler()
        ja_existe_func = list(filter(lambda x: x.cpf == cpf, all_funcs))    
        if ja_existe_func:
            funcionario_novo = Funcionario(clt_nova, salario_novo, nome_novo, idade_nova, cpf, telefone_novo, email_novo, endereco_novo)
            all_funcs = list(map(lambda x: funcionario_novo if (x.cpf == cpf) else (x), all_funcs ))
            DaoFuncionario.limpar()
            for func in all_funcs:
                DaoFuncionario.salvar(func)
            print(f'Funcionário de CPF: {cpf} modificado com sucesso.')
        else:
            print(f'Não existe um funcionário cadastrado com o CPF: {cpf}')
    def exi_funcionarios(self):
        all_funcs = DaoFuncionario.ler()
        if all_funcs:
            for func in all_funcs:
                print(f'Funcionário: {func.nome.upper()}, CPF: {func.cpf}, Salário: {func.salario}, Idade: {func.idade}, E-mail: {func.email}')
        else:
            print(f'Não existe nenhum funcionário cadastrado.')       

class ControllerCliente:
    def cad_cliente(self, nome, idade, cpf, telefone, email, endereco):
        all_clients = DaoCliente.ler()
        ja_existe_cli = list(filter(lambda x: x.cpf == cpf, all_clients))
        if not ja_existe_cli:
            DaoCliente.salvar(Cliente(nome, idade, cpf, telefone, email, endereco))
            print(f'Clinte com CPF: {cpf} cadastrado com sucesso.')
        else:
            print(f'Já existe um cliente cadastrado com o CPF: {cpf}')
    def del_cliente(self, cpf):
        all_clients = DaoCliente.ler()
        ja_existe_cli = list(filter(lambda x: x.cpf == cpf, all_clients))        
        if ja_existe_cli:
            for i in range(len(all_clients)):
                if all_clients[i].cpf == cpf:
                    del all_clients[i]
                    break
            DaoCliente.limpar()    
            for cliente in all_clients:    
                DaoCliente.salvar(cliente)
            print(f'Clinte com CPF: {cpf} excluído com sucesso.')
        else:
            print(f'Não existe um cliente cadastrado com o CPF: {cpf}')
    def alt_cliente(self, nome_novo, idade_nova, cpf, telefone_novo, email_novo, endereco_novo):
        all_clis = DaoCliente.ler()
        ja_existe_cli = list(filter(lambda x: x.cpf == cpf, all_clis))    
        if ja_existe_cli:
            cliente_novo = Cliente(nome_novo, idade_nova, cpf, telefone_novo, email_novo, endereco_novo)
            all_clis = list(map(lambda x: cliente_novo if (x.cpf == cpf) else (x), all_clis ))
            DaoCliente.limpar()
            for func in all_clis:
                DaoCliente.salvar(func)
            print(f'Cliente de CPF: {cpf} modificado com sucesso.')
        else:
            print(f'Não existe um cliente cadastrado com o CPF: {cpf}')
    def exi_clientes(self):
        all_clis = DaoCliente.ler()
        if all_clis:
            for cli in all_clis:
                print(f'Cliente: {cli.nome.upper()}, CPF: {cli.cpf}, Idade: {cli.idade}, E-mail: {cli.email}')
        else:
            print(f'Não existe nenhum cliente cadastrado.') 
