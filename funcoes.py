from random import randint
lista_produtos = []
quantidade_total = 0
valor_total = 0

def menu():
    print('''
1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto
4 - Atualizar produto
5 - Remover produto
6 - Relatorio de estoque
0 - Sair''')
    

def separacao_funcoes():
    print('-' * 50)



def printar_informacoes_produtos(produto):
    separacao_funcoes()
    print(f'Codigo: {produto['codigo']}')
    print(f'Nome: {produto['nome']}')
    print(f'Categoria: {produto['categoria']}')
    print(f'Quantidade: {produto['quantidade']}')
    print(f'Valor {produto['valor']}')
    separacao_funcoes()


def cadastrar_produto():
    nome = input('Informe o nome do produto: ')
    categoria = input('Informe o nome da categoria: ')
    quantidade = int(input('Informe a quantidade do produto: '))
    valor = float(input('Informe o valor do produto: '))

    produto = {
        'codigo': randint(1000, 9999),
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'valor': valor
    }
    lista_produtos.append(produto)

    print('\nProduto cadastrado!!')


def listar_produtos():
    if len(lista_produtos) >= 1:
        for produto in lista_produtos:
            printar_informacoes_produtos(produto)
        return
    
    print('\nNão a produtos cadastrados!!')


def buscar_produto(nome,codigo):
    if len(lista_produtos) >= 1:
        for produto in lista_produtos:
            if nome == produto['nome'] or codigo == produto['codigo']:
                printar_informacoes_produtos(produto)
            else:
                print('Não existe esse produto cadastrado! Tente novamente!!')
            return
        
    print('\nNão a produtos cadastrados!!')
        

def atualizar_produto(nome,codigo):
    if len(lista_produtos) >= 1:
        for produto in lista_produtos:
            if nome == produto['nome'] or codigo == produto['codigo']:
                produto_alterado = input('''
1 - Nome
2 - Categoria
3 - Quantidade
4 - Preço
                                         
Oque deseja alterar: ''')
                
                match produto_alterado:
                    case '1':
                        nome_novo = input('\nQual o novo produto: ')
                        produto['nome'] = nome_novo
                        return

                    case '2':
                        categoria_nova = input('Informe o nome da nova categoria: ')
                        produto['categoria'] = categoria_nova
                        return

                    case '3':
                        quantidade_nova = int(input('Informe a nova quantidade: '))
                        produto['quantidade'] = quantidade_nova
                        return

                    case '4':
                        preco_novo = float(input('Informe o novo preço do produto: '))
                        produto['valor'] = preco_novo
                        return
                    case _:
                        print('Opção invalida!!')
                
                print('\nProduto atualizado!!')
                    
            else:
                print('Não a produto cadastrado com esse nome: ')
                return

    print('\nNão a produtos cadastrados!!')
                    

def remover_produto(nome,codigo):
    if len(lista_produtos) >= 1:
        for produto in lista_produtos:
            if nome == produto['nome'] or codigo == produto['codigo']:
                lista_produtos.remove(produto)
                print('\nProduto removido!!')
            else:
                print('Não a produto cadastrado com esse nome!!')

            return
            
    print('\nNão a produtos cadastrados!!')
                


def relatorio_estoque():
    global quantidade_total
    global valor_total
    if len(lista_produtos) >= 1:
        for produto in lista_produtos:
            quantidade_total += produto['quantidade']
            valor_total += produto['valor']
        print(f'Quantidade total de produtos: {quantidade_total}')
        print(f'Valor total dos produtos: {valor_total}')
        return


    print('\nNão a produtos cadastrados!!')
        


