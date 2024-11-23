import uuid
from datetime import datetime

class FonteReceita:
    def __init__(self, id=None, id_cliente=None, nome_fonte='', valor=0.0, data_recebimento=None, descricao='', criado_por=None, atualizado_por=None):
        self.id = id or uuid.uuid4()
        self.id_cliente = id_cliente
        self.nome_fonte = nome_fonte
        self.valor = valor
        self.data_recebimento = data_recebimento or datetime.now().date()
        self.descricao = descricao
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.criado_por = criado_por
        self.atualizado_por = atualizado_por
