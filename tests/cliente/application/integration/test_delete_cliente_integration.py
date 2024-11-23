from datetime import datetime
from src.core.cliente.application.use_case.delete_cliente import DeleteCliente, DeleteClienteRequest
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.infra.in_memory_cliente_repository import InMemoryClienteRepository


class TestDeleteCliente:
    def test_delete_cliente_from_repository(self):
        cliente1 = Cliente(
            nome="Ráder",
            email="email@example.com",
            is_active=True,
            criado_por="Admin",
            atualizado_por="Admin",
            data_criacao=datetime(2023, 1, 1, 12, 0),
            data_atualizacao=datetime(2023, 1, 1, 12, 0)
        )
        cliente2 = Cliente(
            nome="Bruna",
            email="brunaeverton@live.com",
            is_active=True,
            criado_por="Admin",
            atualizado_por="Admin",
            data_criacao=datetime(2023, 1, 2, 12, 0),
            data_atualizacao=datetime(2023, 1, 2, 12, 0),
        )

        repository = InMemoryClienteRepository(
            clientes=[cliente1, cliente2]
        )

        use_case = DeleteCliente(repository=repository)
        request = DeleteClienteRequest(id=cliente1.id)

        assert repository.get_by_id(cliente1.id) is not None
        response = use_case.execute(request)

        assert repository.get_by_id(cliente1.id) is None
        assert response is None

     