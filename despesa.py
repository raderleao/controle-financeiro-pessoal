import uuid
from datetime import datetime

class Despesa:
    def __init__(self, id=None, id_cliente=None, id_pessoa=None, id_credor=None, descricao='', valor_total=0.0, data_compra=None, data_primeiro_vencimento=None, parcelada=False, numero_parcelas=1, tipo_despesa='', essencial=False, criado_por=None, atualizado_por=None):
        self.id = id or uuid.uuid4()
        self.id_cliente = id_cliente
        self.id_pessoa = id_pessoa
        self.id_credor = id_credor
        self.descricao = descricao
        self.valor_total = valor_total
        self.data_compra = data_compra or datetime.now().date()
        self.data_primeiro_vencimento = data_primeiro_vencimento or datetime.now().date()
        self.parcelada = parcelada
        self.numero_parcelas = numero_parcelas
        self.tipo_despesa = tipo_despesa
        self.essencial = essencial
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.criado_por = criado_por
        self.atualizado_por = atualizado_por
