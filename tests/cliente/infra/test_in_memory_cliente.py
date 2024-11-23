from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.infra.in_memory_cliente_repository import InMemoryClienteRepository


class TestSave:
    def test_can_Save_cliente(self):
        repository = InMemoryClienteRepository()
        cliente = Cliente(
            nome="Ráder",
            email="radeder@example.com"
        )

        repository.save(cliente)

        assert len(repository.clientes) == 1
        assert repository.clientes[0] == cliente

    class TestGetById:
        def test_can_get_cliente_by_id(self):
            
            cliente1 = Cliente(
                nome="Ráder",
                email="radeder@example.com"
            )
            cliente2 = Cliente(
                nome="Bruna",
                email="bruna@example.com",
            )
            repository = InMemoryClienteRepository(
                clientes=[
                    cliente1,
                    cliente2,
                ]
            )

            cliente = repository.get_by_id(cliente1.id)

            assert cliente == cliente1
