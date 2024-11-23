from dataclasses import dataclass
from datetime import datetime

from src.core.cliente.application.repository.cliente_repository import ClienteRepository
from src.core.cliente.domain.exceptions import ClienteNotFound
from uuid import UUID

@dataclass
class DeleteClienteRequest:
    id: UUID
   

class DeleteCliente:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def execute(self, request: DeleteClienteRequest) -> None:
        cliente = self.repository.get_by_id(id=request.id)

        if cliente is None:
            raise ClienteNotFound(f"Cliente with id {request.id} not found in repository {type(self.repository).__name__}")

        self.repository.delete(cliente.id) 
