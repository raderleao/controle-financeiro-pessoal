from typing import List
from uuid import UUID
from src.core.cliente.application.repository.cliente_repository import ClienteRepository
from src.core.cliente.domain.cliente import Cliente


class InMemoryClienteRepository(ClienteRepository):
    def __init__(self, clientes=None):
        self.clientes = clientes or []

    def save(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def list(self, ativos: bool = None) -> List[Cliente]:
        if ativos is None:
            return self.clientes
        return [cliente for cliente in self.clientes if cliente.is_active == ativos]

    def get_by_id(self, id: UUID) -> Cliente | None:
        return next(
            (cliente for cliente in self.clientes if cliente.id == id), None
        )
    
    def delete(self, id: UUID) -> None:
        cliente = self.get_by_id(id)
        self.clientes.remove(cliente)