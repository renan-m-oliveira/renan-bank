class Cliente:
    def __init__(self, id, nome, idade, renda, saldo=0):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.renda = renda
        self.saldo = saldo
        self.historico = []

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "renda": self.renda,
            "saldo": self.saldo,
            "historico": self.historico
        }