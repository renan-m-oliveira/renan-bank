import json  # Biblioteca para ler e escrever arquivos JSON
import os    # Biblioteca para verificar se o arquivo existe no sistema

ARQUIVO = "clientes.json"  # Nome do arquivo onde os clientes são salvos


def salvar_clientes(clientes):  # Função que salva a lista de clientes no arquivo JSON
    with open(ARQUIVO, "w", encoding="utf-8") as f:  # Abre o arquivo para escrita com suporte a acentos
        json.dump([c.to_dict() for c in clientes], f, indent=4, ensure_ascii=False)  # Converte cada cliente em dicionário e salva formatado


def carregar_clientes():  # Função que carrega os clientes salvos no arquivo JSON
    if not os.path.exists(ARQUIVO):  # Se o arquivo ainda não existe
        return []                    # Retorna lista vazia
    with open(ARQUIVO, "r", encoding="utf-8") as f:  # Abre o arquivo para leitura com suporte a acentos
        return json.load(f)  # Lê o JSON e retorna como lista de dicionários
