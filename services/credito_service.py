from models.clientee import Cliente
from database.json_db import salvar_clientes


def solicitar_emprestimo(clientes):
    print("--- Solicitação de Empréstimo ---")
    while True:
        try:
            id_busca = int(input("Digite o ID do cliente: "))
            break
        except ValueError:
            print ("Digite apenas números!")
    for cliente in clientes:
        if cliente.id == id_busca:
            print(f"Cliente: {cliente.nome}")
            print(f"Renda mensal: R$ {cliente.renda:.2f}")
            while True:
                try:
                    valor = float(input("Valor do empréstimo solicitado: R$ "))
                    break
                except ValueError:
                    print ("Digite apenas números!")

            if valor <= 0:
                print("Valor inválido.")
                return

            limite = cliente.renda * 3
            if valor > limite:
                print(f"Empréstimo negado. Limite máximo: R$ {limite:.2f}")
            else:
                cliente.saldo += valor
                salvar_clientes(clientes)
                print(f"Empréstimo de R$ {valor:.2f} aprovado!")
                print(f"Novo saldo: R$ {cliente.saldo:.2f}")
            return cliente

    print("Cliente não encontrado.")
    return None