from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.domain.repository.cliente_repository import ClienteRepository
from src.core.cliente.domain.exceptions import ClienteNotFound
import uuid


class ActivateCliente:
    def __init__(self, repository: ClienteRepository):
        """
        Inicializa o caso de uso com o repositório necessário.
        :param repository: Repositório que implementa ClienteRepository.
        """
        self.repository = repository

    def execute(self, cliente_id: uuid.UUID, alterado_por: str):
        """
        Ativa o cliente especificado pelo ID.
        :param cliente_id: ID do cliente a ser ativado.
        :param alterado_por: Nome ou identificador de quem realizou a ativação.
        """
        # Busca o cliente no repositório
        cliente = self.repository.get_by_id(cliente_id)
        if not cliente:
            raise ClienteNotFound(cliente_id)

        # Ativa o cliente
        cliente.activate(alterado_por=alterado_por)

        # Salva o cliente atualizado no repositório
        self.repository.save(cliente)
