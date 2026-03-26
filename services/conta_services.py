from datetime import datetime              # Importa datetime para registrar data e hora das transações
from models.clientee import Cliente        # Importa a classe Cliente
from database.json_db import salvar_clientes  # Importa função para salvar no JSON

def depositar_valor (clientes):  # Função que realiza um depósito na conta do cliente
    while True:  # Loop de validação do ID
        try:
            id_busca = int(input ("Digite o seu id para continuar..."))
            break  # Sai do loop se for número válido
        except ValueError:
            print ("Digite apenas números ! ")

    for cliente in clientes:  # Percorre a lista procurando o ID informado
        if cliente.id == id_busca:
            print ("CONFIRME SEU NOME ANTES DE CONTIUNUAR.......")  # Pede confirmação do nome
            print (cliente.nome)
            print (f"Saldo atual: {cliente.saldo:.2f}")

            while True:  # Loop de validação do valor do depósito
                try:
                    Valor_depostio = float(input("Qual o valor que deseja depositar ? "))
                    break  # Sai do loop se for número válido
                except ValueError:
                    print ("Digite apeans números !")

            cliente.saldo = cliente.saldo +Valor_depostio  # Soma o valor depositado ao saldo
            cliente.historico.append({                     # Registra a transação no histórico
            "tipo": "Depósito",
            "valor": Valor_depostio,
            "data": datetime.now().strftime ("%d/%m/%Y %H:%M")  # Data e hora atual formatada
            })
            salvar_clientes (clientes)  # Salva as alterações no arquivo JSON
            print ("Deposito realizado com sucesso ! ")
            print (f"Seu saldo agora é de:  {cliente.saldo:.2f}")
            return cliente  # Retorna o objeto do cliente


    print("Cliente não encontrado.")
    return None


def saque (clientes):  # Função que realiza um saque na conta do cliente
    while True:  # Loop de validação do ID
        try:
            id_busca = int(input("Digite seu id para continuar..."))
            break  # Sai do loop se for número válido
        except ValueError:
            print("Digite apenas números ! ")

    for cliente in clientes:  # Percorre a lista procurando o ID informado
        if cliente.id == id_busca:
            print ("CONFIRME SEU NOME ANTES DE CONTIUNUAR.......")  # Pede confirmação do nome
            print (cliente.nome)
            while True:  # Loop que aguarda confirmação do usuário (s/n)
                try:
                    resposta = input("Deseja continuar ? (s/n)")
                    if resposta == "s":
                        print (f"Saldo atual: {cliente.saldo:.2f}")  # Exibe saldo antes do saque
                        while True:  # Loop de validação do valor do saque
                            try:
                                valor_saque = float(input("Digite o valor que deseja sacar... "))
                                if cliente.saldo >= valor_saque:  # Verifica se tem saldo suficiente
                                    cliente.saldo -= valor_saque  # Subtrai o valor do saldo
                                    cliente.historico.append ({   # Registra a transação no histórico
                                    "tipo": "Saque",
                                    "valor": valor_saque,
                                    "data": datetime.now().strftime ("%d/%m/%Y %H:%M")  # Data e hora atual
                                    })
                                    salvar_clientes(clientes)  # Salva as alterações no arquivo JSON
                                    print("Saque realizado com sucesso. ")
                                    print (f"Seu saldo agora é de {cliente.saldo:.2f}")
                                    return cliente  # Retorna o objeto do cliente
                                else:
                                    print ("Saldo insuficiente !")  # Avisa saldo insuficiente
                                    break
                            except ValueError:
                                print("Digite apenas números ! ")
                    elif resposta == "n":
                        break  # Usuário cancelou o saque
                except ValueError:
                    print ("Resposta inválida ! ")
    else:
        print("CLiente não encontrado ! ")  # ID não encontrado na lista
        return None



def mostrar_saldo (clientes):  # Função que exibe o saldo atual do cliente
    while True:  # Loop que repete até encontrar o cliente ou receber ID válido
        try:
            id_busca = int(input("Digite seu id "))
            for cliente in clientes:  # Percorre a lista procurando o ID informado
                if cliente.id == id_busca:
                    print (f"Nome: {cliente.nome}, Saldo: {cliente.saldo:.2f}")
                    return  # Encerra após exibir o saldo
            else:
                print ("Cliente não encontrado")  # ID não encontrado na lista
        except ValueError:
            print ("Digite apenas números ! ")


def pix (clientes):  # Função que realiza um pix de um cliente para outro
    while True:  # Loop que repete até completar ou cancelar o pix
        try:
            id_busca = int(input("Digite seu id  "))
            for cliente in clientes:  # Percorre a lista procurando o remetente
                if cliente.id == id_busca:
                    print (f"Nome: {cliente.nome}  Saldo: {cliente.saldo:.2f}")
                    valor_pix = float(input("Digite o valor do pix :   "))
                    if cliente.saldo >= valor_pix:  # Verifica se tem saldo suficiente
                        cliente.saldo -= valor_pix  # Debita o valor do remetente
                        cliente.historico.append ({  # Registra a saída no histórico do remetente
                        "tipo": "Pix enviado",
                        "valor": valor_pix,
                        "data": datetime.now().strftime ("%d/%m/%Y %H:%M")  # Data e hora atual
                        })

                        id_destino = int(input("Digite o id para quem vc deseja enviar" ))
                        for cliente_destino in clientes:  # Percorre a lista procurando o destinatário
                            if cliente_destino.id == id_destino:
                                cliente_destino.saldo += valor_pix  # Credita o valor no destinatário
                                cliente_destino.historico.append ({  # Registra o recebimento no histórico do destinatário
                                    "tipo": "Pix recebido",
                                    "valor": valor_pix,
                                    "data": datetime.now().strftime ("%d/%m/%Y %H:%M")  # Data e hora atual
                                                })
                                salvar_clientes (clientes)  # Salva as alterações de ambos no JSON
                                print ("PIX enviado com sucesso ! ")
                                return  # Encerra após enviar o pix
                        else:
                            print("Destinatário não encontrado!")
                            cliente.saldo += valor_pix  # ← devolve o dinheiro ao remetente
                            return

                    else:
                        print ("Saldo insuficente ! ")  # Avisa saldo insuficiente
                        return
            else:
                print("Cliente não encontrado!")  # ID do remetente não encontrado
                return


        except ValueError:
            print("Digite apenas numeros")


def mostrar_extrato (clientes):  # Função que exibe o extrato de transações do cliente
    while True:  # Loop que repete até mostrar o extrato ou receber ID válido
        try:
            id_busca = int(input("Digite seu id:  "))
            for cliente in clientes:  # Percorre a lista procurando o ID informado
                if cliente.id == id_busca:
                    print (f"----- Extrato da conta de {cliente.nome}-----")
                    if not cliente.historico:  # Verifica se há transações registradas
                        print ("Nenhuma transação encontrada")
                        return  # Encerra se não houver transações
                    for transacao in cliente.historico:  # Percorre cada transação e exibe
                        print(f"Tipo:  {transacao['tipo']}")           # Tipo: Depósito, Saque, Pix
                        print(f"Valor: R$ {transacao['valor']:.2f}")   # Valor da transação
                        print(f"Data:  {transacao['data']}")           # Data e hora
                        print("---------------------------")
                    return  # Encerra após exibir todo o extrato
            else:
                print("Cliente não encontrado!")  # ID não encontrado na lista
        except ValueError:
            print("Digite apenas números!")




