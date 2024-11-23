import uuid
from datetime import datetime

class DadosBancarios:
    def __init__(self, id=None, id_credor=None, tipo_chave_pix='', descricao_chave_pix='', banco='', agencia='', numero_conta='', criado_por=None, atualizado_por=None):
        self.id = id or uuid.uuid4()
        self.id_credor = id_credor
        self.tipo_chave_pix = tipo_chave_pix
        self.descricao_chave_pix = descricao_chave_pix
        self.banco = banco
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.criado_por = criado_por
        self.atualizado_por = atualizado_por
