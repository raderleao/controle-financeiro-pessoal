from unittest import TestCase
import uuid
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.domain.exceptions import ClienteNotFound
from src.core.cliente.infra.in_memory_cliente_repository import InMemoryClienteRepository
from src.core.cliente.application.use_case.actions.update_cliente import UpdateCliente

class TestUpdateClienteIntegration(TestCase):
    def setUp(self):
        self.repository = InMemoryClienteRepository()
        self.cliente = Cliente(nome="João Silva", email="joao.silva@example.com")
        self.repository.save(self.cliente)
        self.use_case = UpdateCliente(repository=self.repository)

    def test_update_cliente_nome(self):
        request = UpdateCliente.Request(id=self.cliente.id, nome="João Carlos")
        self.use_case.execute(request)

        cliente_atualizado = self.repository.get_by_id(self.cliente.id)
        self.assertEqual(cliente_atualizado.nome, "João Carlos")

    def test_update_cliente_not_found(self):
        request = UpdateCliente.Request(id=uuid.uuid4(), nome="Novo Nome")
        with self.assertRaises(ClienteNotFound):
            self.use_case.execute(request)
