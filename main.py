from funcoes import *

print('###  SISTEMA DE PRODUTOS  🛒🛒  ###')


while True:
    menu()
    opcoes = input('Informe a opção escolhida: ')
    match opcoes:
        case '1':
            cadastrar_produto()

        case '2':
            listar_produtos()

        case '3':
            nome_buscar = input('Informe o nome do produto: ')
            codigo_buscar = int(input('Informe o codigo do produto: '))
            buscar_produto(nome_buscar,codigo_buscar)

        case '4':
            nome_atualizar = input('Informe o nome do produto: ')
            codigo_atualizar = int(input('Informe o codigo do produto: '))
            atualizar_produto(nome_atualizar,codigo_atualizar)

        case '5':
            nome_remover = input('Informe o nome do produto que deseja remover: ')
            codigo_remover = int(input('Informe o codigo do produto que deseja remover: '))
            remover_produto(nome_remover,codigo_remover)

        case '6':
            relatorio_estoque()

        case '0':
            print('Volte sempre!!')
            break

        case _:
            print('Opção invalida!!')
            
            
