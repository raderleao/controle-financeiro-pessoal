from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from src.core.cliente.domain.repository.cliente_repository import ClienteRepository

@dataclass
class ListClienteRequest:
    """Request para listar clientes (podem ser adicionados filtros no futuro)."""
    ativos: bool = None  


@dataclass
class ClienteOutPut:
    """Representação de saída de um cliente."""
    id: UUID
    nome: str
    email: str
    is_active: bool
    criado_por: str
    atualizado_por: str
    data_criacao: datetime
    data_atualizacao: datetime
    historico_alteracoes: list  


@dataclass
class ListClienteResponse:
    """Resposta com a lista de clientes."""
    data: list[ClienteOutPut]


class ListCliente:
    def __init__(self, repository: ClienteRepository):
        self.repository = repository

    def execute(self, request: ListClienteRequest) -> ListClienteResponse:
        # Obter a lista de clientes do repositório, com ou sem filtro
        clientes = self.repository.list(ativos=request.ativos)

        # Converter a lista de clientes em objetos ClienteOutPut
        return ListClienteResponse(
            data=[
                ClienteOutPut(
                    id=cliente.id,
                    nome=cliente.nome,
                    email=cliente.email,
                    is_active=cliente.is_active,
                    criado_por=cliente.criado_por,
                    atualizado_por=cliente.atualizado_por,
                    data_criacao=cliente.data_criacao,
                    data_atualizacao=cliente.data_atualizacao,
                    historico_alteracoes=cliente.historico_alteracoes, 
                ) for cliente in clientes
            ]
        )
