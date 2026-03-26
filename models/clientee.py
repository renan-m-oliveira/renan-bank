class Cliente:  # Classe que representa cada cliente do banco
    def __init__(self, id, nome, idade, renda, saldo=0, historico = None):  # Construtor do cliente
        self.id = id            # ID único do cliente
        self.nome = nome        # Nome do cliente
        self.idade = idade      # Idade do cliente
        self.renda = renda      # Renda mensal do cliente
        self.saldo = saldo      # Saldo da conta do cliente
        self.historico = historico if historico is not None else []  # Lista de transações (vazia se não informada)

    def to_dict(self):  # Converte o objeto em dicionário para salvar no JSON
        return {
            "id": self.id,               # ID do cliente
            "nome": self.nome,           # Nome do cliente
            "idade": self.idade,         # Idade do cliente
            "renda": self.renda,         # Renda mensal
            "saldo": self.saldo,         # Saldo atual
            "historico": self.historico  # Lista de transações
        }
