from unittest import TestCase
from src.core.cliente.application.use_case.actions.activate_cliente import ActivateCliente
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.infra.in_memory_cliente_repository import InMemoryClienteRepository


class TestActivateClienteIntegration(TestCase):
    def setUp(self):
        self.repository = InMemoryClienteRepository()
        self.cliente = Cliente(nome="João Silva", email="joao.silva@example.com", is_active=False)
        self.repository.save(self.cliente)
        self.use_case = ActivateCliente(repository=self.repository)

    def test_activate_cliente(self):
        self.use_case.execute(cliente_id=self.cliente.id, alterado_por="Admin")

        cliente_ativado = self.repository.get_by_id(self.cliente.id)
        self.assertTrue(cliente_ativado.is_active)
