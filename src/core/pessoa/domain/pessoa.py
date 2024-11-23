
import uuid
from datetime import datetime

class Pessoa:
    def __init__(self, id=None, id_cliente=None, nome='', cpf='', email='', telefone='', criado_por=None, atualizado_por=None):
        self.id = id or uuid.uuid4()
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.criado_por = criado_por
        self.atualizado_por = atualizado_por
