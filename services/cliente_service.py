from models.clientee import Cliente
from database.json_db import salvar_clientes


def cadastrar_cliente(clientes):
    print("--- Cadastro de Cliente ---")
    while True:
            nome = input("Nome: ")
            if nome.replace (" ", "").isalpha ():
                break
            else:
                print ("Nome inválido, digite apenas letras! ")
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print ("Digite apenas números")

    while True:
        try:
            renda = float(input("Renda mensal: R$ "))
            break
        except ValueError:
            print ("Digite apenas números")
    id_cliente = max(c.id for c in clientes) + 1

    cliente = Cliente(id_cliente, nome, idade, renda)
    clientes.append(cliente)
    salvar_clientes(clientes)
    print(f"Cliente '{nome}' cadastrado com sucesso! ID: {id_cliente}")


def mostrar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    print("--- Lista de Clientes ---")
    for cliente in clientes:
        print("---------------------------")
        print(f"ID:           {cliente.id}")
        print(f"Nome:         {cliente.nome}")
        print(f"Idade:        {cliente.idade} anos")
        print(f"Renda mensal: R$ {cliente.renda:.2f}")
        print(f"Saldo:        R$ {cliente.saldo:.2f}")
    print("---------------------------")


def buscar_cliente(clientes):
    while True:
        try:
            id_busca = int(input("Digite o ID do cliente: "))
            break
        except ValueError:
            print ("Digite apenas números")
    for cliente in clientes:
        if cliente.id == id_busca:
            print("---------------------------")
            print(f"ID:           {cliente.id}")
            print(f"Nome:         {cliente.nome}")
            print(f"Idade:        {cliente.idade} anos")
            print(f"Renda mensal: R$ {cliente.renda:.2f}")
            print(f"Saldo:        R$ {cliente.saldo:.2f}")
            print("---------------------------")
            return cliente

    print("Cliente não encontrado.")
    return None


def excluir_cliente(clientes):
    while True:
        try:
            id_busca = int(input("Digite o ID do cliente que deseja excluir: "))
            break  
        except ValueError:
            print ("Digite apenas números")
    for cliente in clientes:
        if cliente.id == id_busca:
            clientes.remove(cliente)
            salvar_clientes(clientes)
            print(f"Cliente '{cliente.nome}' removido com sucesso.")
            return

    print("Cliente não encontrado.")
