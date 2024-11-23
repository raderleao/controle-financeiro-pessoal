import uuid
from datetime import datetime

class Parcela:
    def __init__(self, id=None, id_despesa=None, valor=0.0, data_vencimento=None, status_pagamento='pendente', criado_por=None, atualizado_por=None):
        self.id = id or uuid.uuid4()
        self.id_despesa = id_despesa
        self.valor = valor
        self.data_vencimento = data_vencimento or datetime.now().date()
        self.status_pagamento = status_pagamento
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.criado_por = criado_por
        self.atualizado_por = atualizado_por
