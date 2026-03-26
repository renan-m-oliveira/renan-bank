import services.cliente_service as cliente_service  # Módulo com funções de clientes
import services.conta_services as conta_services    # Módulo com funções de conta
import services.credito_service as credito_service  # Módulo com funções de crédito
from database.json_db import carregar_clientes       # Função que lê os dados do arquivo JSON
from models.clientee import Cliente                  # Classe que representa um cliente

dados = carregar_clientes()  # Carrega os dados brutos (dicionários) do arquivo JSON

# Transforma cada dicionário carregado do JSON em um objeto Cliente e salva na lista
clientes = [Cliente(d["id"], d["nome"], d["idade"], d["renda"], d["saldo"], d["historico"]) for d in dados]


def menu_principal(clientes):
    while True:  # Loop que mantém o menu rodando até o usuário sair
        print("=========SISTEMA DE CRÉDITO RENAN BANK==========")
        print("1 - Serviços de clientes")
        print("2 - Serviços de crédito")
        print("3 - Serviços de conta")
        print("4 - Sair do sistema")

        opcao = int(input("Escolha uma opção: "))  # Lê e converte a opção para inteiro

        if opcao == 1:
            menu_clientes(clientes)   # Vai para o menu de clientes
        elif opcao == 2:
            menu_credito(clientes)    # Vai para o menu de crédito
        elif opcao == 3:
            menu_conta(clientes)      # Vai para o menu de conta
        elif opcao == 4:
            print("Saindo do sistema...")
            return  # Encerra o sistema
        else:
            print("Opção inválida, escolha entre 1 e 4!")


def menu_clientes(clientes):
    while True:  # Loop que mantém o menu aberto até o usuário voltar
        print("\n========MENU CLIENTES ==========")
        print("1 - Cadastrar cliente")
        print("2 - Mostrar clientes")
        print("3 - Buscar cliente por ID")
        print("4 - Excluir cliente")
        print("5 - Voltar ao menu principal")

        while True:  # Loop de validação: repete até receber um número válido
            try:
                opcao = int(input("Escolha uma opção: "))
                break  # Sai do loop se for número válido
            except ValueError:
                print("Resposta inválida, escolha uma opção!")  # Avisa entrada inválida

        if opcao == 1:
            cliente_service.cadastrar_cliente(clientes)   # Chama função de cadastro
        elif opcao == 2:
            cliente_service.mostrar_clientes(clientes)    # Chama função de listagem
        elif opcao == 3:
            cliente_service.buscar_cliente(clientes)      # Chama função de busca por ID
        elif opcao == 4:
            cliente_service.excluir_cliente(clientes)     # Chama função de exclusão
        elif opcao == 5:
            return  # Volta ao menu principal
        else:
            print("Opção inválida!")


def menu_credito(clientes):
    while True:  # Loop que mantém o menu aberto até o usuário voltar
        print("\n========MENU CRÉDITO ==========")
        print("1 - Solicitar empréstimo")
        print("2 - Voltar para o menu principal")

        while True:  # Loop de validação: repete até receber um número válido
            try:
                opcao = int(input("Escolha uma opção: "))
                break  # Sai do loop se for número válido
            except ValueError:
                print("Resposta inválida!")  # Avisa entrada inválida

        if opcao == 1:
            credito_service.solicitar_emprestimo(clientes)  # Chama função de empréstimo
        elif opcao == 2:
            return  # Volta ao menu principal
        else:
            print("Opção inválida!")


def menu_conta(clientes):
    while True:  # Loop que mantém o menu aberto até o usuário voltar
        print("\n=========MENU CONTA==========")
        print("1 - Realizar depósito")
        print("2 - Realizar saque")
        print("3 - Consultar saldo ")
        print("4 - Pix ")
        print("5 - Mostrar extrato conta ")
        print("6 - Voltar para o menu principal")

        while True:  # Loop de validação: repete até receber um número válido
            try:
                opcao = int(input("Escolha uma opção: "))
                break  # Sai do loop se for número válido
            except ValueError:
                print("Resposta inválida, escolha uma opção!")  # Avisa entrada inválida

        if opcao == 1:
            conta_services.depositar_valor(clientes)   # Chama função de depósito
        elif opcao == 2:
            conta_services.saque(clientes)             # Chama função de saque
        elif opcao == 3:
            conta_services.mostrar_saldo(clientes)     # Chama função de consulta de saldo
        elif opcao == 4:
            conta_services.pix (clientes)              # Chama função de pix
        elif opcao == 5:
            conta_services.mostrar_extrato (clientes)  # Chama função de extrato
        elif opcao == 6:
            return  # Volta ao menu principal
        else:
            print("Opção inválida!")


menu_principal(clientes)  # Inicia o sistema chamando o menu principal
