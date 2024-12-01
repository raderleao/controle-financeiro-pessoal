from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from src.core.cliente.domain.cliente import Cliente

class ClienteRepository(ABC):
    @abstractmethod
    def save(self, cliente):
        raise NotImplementedError
    
    @abstractmethod
    def list(self, ativos: bool = None) -> List[Cliente]:
        pass
    
    @abstractmethod
    def get_by_id(self, id:UUID) -> Cliente | None:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id:UUID) -> None:
        raise NotImplementedError