import json
import os

ARQUIVO = "clientes.json"


def salvar_clientes(clientes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump([c.to_dict() for c in clientes], f, indent=4, ensure_ascii=False)


def carregar_clientes():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)