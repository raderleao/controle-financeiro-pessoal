import uuid
from datetime import datetime

class Pagamento:
    def __init__(self, id=None, id_parcela=None, id_dados_bancarios=None, forma_pagamento='', data_pagamento=None, valor_pagamento=0.0, descricao='', criado_por=None, atualizado_por=None):
        self.id = id or uuid.uuid4()
        self.id_parcela = id_parcela
        self.id_dados_bancarios = id_dados_bancarios
        self.forma_pagamento = forma_pagamento  # Ex.: 'PIX', 'boleto', 'pagamento físico'
        self.data_pagamento = data_pagamento or datetime.now().date()
        self.valor_pagamento = valor_pagamento
        self.descricao = descricao
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.criado_por = criado_por
        self.atualizado_por = atualizado_por
