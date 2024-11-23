import uuid
from datetime import datetime

class Credor:
    def __init__(self, id=None, id_cliente=None, nome='', telefone='', tipo_recebimento='', criado_por=None, atualizado_por=None):
        self.id = id or uuid.uuid4()
        self.id_cliente = id_cliente
        self.nome = nome
        self.telefone = telefone
        self.tipo_recebimento = tipo_recebimento  # Valores como 'transferência', 'PIX', 'outro'
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.criado_por = criado_por
        self.atualizado_por = atualizado_por
