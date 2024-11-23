from dataclasses import dataclass

from src.core.cliente.application.repository.cliente_repository import ClienteRepository
from ...domain.cliente import Cliente
from src.core.cliente.domain.exceptions import InvalidClienteData
from datetime import datetime
from uuid import UUID

@dataclass
class CreateClienteRequest:
    nome: str
    email: str
    is_active: bool = True  # Valor padrão: ativo por padrão
    criado_por: str = None  # Valor padrão: nenhum criador especificado
    atualizado_por: str = None  # Valor padrão: nenhum atualizador especificado

@dataclass
class CreateClienteResponse:
    id: UUID

class CreateCliente:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def execute(self, request: CreateClienteRequest) -> CreateClienteResponse:
        try: 
            request = Cliente(
                nome=request.nome,
                email=request.email,
                is_active=request.is_active,
                criado_por=request.criado_por,
                atualizado_por=request.atualizado_por,
                data_criacao=datetime.now(),
                data_atualizacao=datetime.now()
            )

            self.repository.save(request)
        except ValueError as err:
            raise InvalidClienteData(err)
        
        return CreateClienteResponse(id=request.id)
