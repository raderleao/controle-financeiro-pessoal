from dataclasses import dataclass
from datetime import datetime

from src.core.cliente.domain.repository.cliente_repository import ClienteRepository
from src.core.cliente.domain.exceptions import ClienteNotFound
from uuid import UUID

@dataclass
class GetClienteRequest:
    id: UUID
   
@dataclass
class GetClienteResponse:
    id: UUID
    nome: str
    email: str
    is_active: bool
    criado_por: str
    atualizado_por: str
    data_criacao: datetime
    data_atualizacao: datetime

class GetCliente:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def execute(self, request: GetClienteRequest) -> GetClienteResponse:
        cliente = self.repository.get_by_id(id=request.id)

        if cliente is None:
            raise ClienteNotFound(f"Cliente with id {request.id} not found in repository {type(self.repository).__name__}")


        return GetClienteResponse(
            id=cliente.id,
            nome=cliente.nome,
            email=cliente.email,
            is_active=cliente.is_active,
            criado_por=cliente.criado_por,
            atualizado_por=cliente.atualizado_por,
            data_criacao=cliente.data_criacao,
            data_atualizacao=cliente.data_atualizacao
        )
