from uuid import UUID
from src.core.cliente.application.use_case.create_cliente import CreateCliente, CreateClienteRequest, CreateClienteResponse
from src.core.cliente.infra.in_memory_cliente_repository import InMemoryClienteRepository


class TestCreateCliente:
    def test_create_cliente_with_valid_data(self):
        repository = InMemoryClienteRepository()
        use_case = CreateCliente(repository=repository)
        request = CreateClienteRequest(
            nome="Ráder",
            email="test@example.com",
            is_active=True,
            criado_por="Admin",
            atualizado_por="Admin"
        )

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response.id, UUID)
        assert len(repository.clientes) == 1
        
        persisted_cliente = repository.clientes[0] 
        assert persisted_cliente.id == response.id
        assert persisted_cliente.nome == "Ráder"
        assert persisted_cliente.email == "test@example.com"
        assert persisted_cliente.is_active == True
