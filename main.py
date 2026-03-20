import services.cliente_service as cliente_service
import services.credito_service as credito_service 
from database.json_db import carregar_clientes
from models.clientee import Cliente

dados = carregar_clientes()
clientes = [Cliente(d["id"], d["nome"], d["idade"], d["renda"], d["saldo"]) for d in dados]

def mostrar_menu():
    print("=========SISTEMA DE CRÉDITO RENAN BANK==========")
    print("1 - Cadastrar cliente")
    print("2 - Mostrar clientes")
    print("3 - Solicitar empréstimo")
    print("4 - Buscar cliente por ID")
    print("5 - Excluir cliente")
    print("6 - Sair do sistema")

def menu(clientes):
    while True:
        mostrar_menu()
        while True:
            try:
                opcao = input("Escolha uma opção: ")
                break
            except ValueError:
                print("Digite apenas números!")
        if opcao == "1":
            while True:
                resposta =  input("Deseja continuar (s/n)?")
                if resposta == "s":
                    cliente_service.cadastrar_cliente(clientes)
                elif resposta =="n" :
                    break
                else:
                    print ("Respota inválida !")
        elif opcao == "2":    
             while True:
                resposta = input("Deseja continuar (s/n)?")
                if resposta == "s":
                   cliente_service.mostrar_clientes(clientes)
                elif resposta == "n":
                        break
                else:
                    print ("Respota inválida !")
        elif opcao == "3":
            while True:
                resposta = input("Deseja continuar (s/n)   ?")
                if resposta == ("s"):
                    credito_service.solicitar_emprestimo(clientes)
                elif resposta == "n":
                      break
                else:
                    print ("Respota inválida ! ")
        elif opcao == "4":
            while True:
                resposta = input("Deseja continuar ? (s/n)")
                if resposta == "s":
                    cliente_service.buscar_cliente(clientes)
                elif resposta == "n":
                    break
                else:
                    print ("Resposta inválida ! ")
        elif opcao == "5":
            while True:
                resposta = input("Deseja continuar (s/n)")
                if resposta == "s":
                       cliente_service.excluir_cliente(clientes)
                elif resposta == "n":
                    break
                else:
                    print ("Resposta inválida !")

        elif opcao == "6":
            while True:
                resposta = input ("Deseja sair do sistema ?  (s/n)")
                if resposta == "s":
                    print("Saindo do sistema...")
                    return
                elif resposta == "n":
                    break
                else:
                    print("Opção inválida. Tente novamente.")


menu(clientes)