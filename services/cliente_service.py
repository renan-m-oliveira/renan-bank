from models.clientee import Cliente       # Importa a classe Cliente
from database.json_db import salvar_clientes  # Importa função para salvar no JSON


def cadastrar_cliente(clientes):  # Função que cadastra um novo cliente
    print("--- Cadastro de Cliente ---")
    while True:  # Loop que repete até o usuário digitar um nome válido
            nome = input("Nome: ")
            if nome.replace (" ", "").isalpha ():  # Verifica se o nome tem apenas letras
                break  # Nome válido, sai do loop
            else:
                print ("Nome inválido, digite apenas letras! ")
    while True:  # Loop de validação da idade
        try:
            idade = int(input("Idade: "))
            break  # Sai do loop se for número válido
        except ValueError:
            print ("Digite apenas números")

    while True:  # Loop de validação da renda
        try:
            renda = float(input("Renda mensal: R$ "))
            break  # Sai do loop se for número válido
        except ValueError:
            print ("Digite apenas números")
    id_cliente = max(c.id for c in clientes) + 1  # Gera um novo ID único (maior ID existente + 1)

    cliente = Cliente(id_cliente, nome, idade, renda)  # Cria o objeto Cliente com os dados informados
    clientes.append(cliente)       # Adiciona o novo cliente na lista em memória
    salvar_clientes(clientes)      # Salva a lista atualizada no arquivo JSON
    print(f"Cliente '{nome}' cadastrado com sucesso! ID: {id_cliente}")


def mostrar_clientes(clientes):  # Função que exibe todos os clientes cadastrados
    if not clientes:  # Se a lista estiver vazia, avisa e encerra
        print("Nenhum cliente cadastrado.")
        return

    print("--- Lista de Clientes ---")
    for cliente in clientes:  # Percorre cada cliente e exibe suas informações
        print("---------------------------")
        print(f"ID:           {cliente.id}")
        print(f"Nome:         {cliente.nome}")
        print(f"Idade:        {cliente.idade} anos")
        print(f"Renda mensal: R$ {cliente.renda:.2f}")
        print(f"Saldo:        R$ {cliente.saldo:.2f}")
    print("---------------------------")


def buscar_cliente(clientes):  # Função que busca um cliente pelo ID
    while True:  # Loop de validação do ID
        try:
            id_busca = int(input("Digite o ID do cliente: "))
            break  # Sai do loop se for número válido
        except ValueError:
            print ("Digite apenas números")
    for cliente in clientes:  # Percorre a lista procurando o ID informado
        if cliente.id == id_busca:
            print("---------------------------")
            print(f"ID:           {cliente.id}")
            print(f"Nome:         {cliente.nome}")
            print(f"Idade:        {cliente.idade} anos")
            print(f"Renda mensal: R$ {cliente.renda:.2f}")
            print(f"Saldo:        R$ {cliente.saldo:.2f}")
            print("---------------------------")
            return cliente  # Retorna o cliente encontrado

    print("Cliente não encontrado.")
    return None


def excluir_cliente(clientes):  # Função que remove um cliente da lista pelo ID
    while True:  # Loop de validação do ID
        try:
            id_busca = int(input("Digite o ID do cliente que deseja excluir: "))
            break  # Sai do loop se for número válido
        except ValueError:
            print ("Digite apenas números")
    for cliente in clientes:  # Percorre a lista procurando o ID informado
        if cliente.id == id_busca:
            clientes.remove(cliente)    # Remove o cliente da lista em memória
            salvar_clientes(clientes)   # Salva a lista atualizada no arquivo JSON
            print(f"Cliente '{cliente.nome}' removido com sucesso.")
            return  # Encerra após excluir

    print("Cliente não encontrado.")
