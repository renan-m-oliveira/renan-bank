from models.clientee import Cliente           # Importa a classe Cliente
from database.json_db import salvar_clientes  # Importa função para salvar no JSON


def solicitar_emprestimo(clientes):  # Função que processa a solicitação de empréstimo
    print("--- Solicitação de Empréstimo ---")
    while True:  # Loop de validação do ID
        try:
            id_busca = int(input("Digite o ID do cliente: "))
            break  # Sai do loop se for número válido
        except ValueError:
            print ("Digite apenas números!")
    for cliente in clientes:  # Percorre a lista procurando o ID informado
        if cliente.id == id_busca:
            print(f"Cliente: {cliente.nome}")
            print(f"Renda mensal: R$ {cliente.renda:.2f}")
            while True:  # Loop de validação do valor do empréstimo
                try:
                    valor = float(input("Valor do empréstimo solicitado: R$ "))
                    break  # Sai do loop se for número válido
                except ValueError:
                    print ("Digite apenas números!")

            if valor <= 0:  # Verifica se o valor é maior que zero
                print("Valor inválido.")
                return  # Encerra sem aprovar

            limite = cliente.renda * 3  # Limite máximo = 3 vezes a renda mensal
            if valor > limite:  # Se pediu mais que o limite, nega
                print(f"Empréstimo negado. Limite máximo: R$ {limite:.2f}")
            else:
                cliente.saldo += valor          # Adiciona o valor ao saldo do cliente
                salvar_clientes(clientes)       # Salva as alterações no arquivo JSON
                print(f"Empréstimo de R$ {valor:.2f} aprovado!")
                print(f"Novo saldo: R$ {cliente.saldo:.2f}")
            return cliente  # Retorna o objeto do cliente

    print("Cliente não encontrado.")
    return None


