from unittest import TestCase

from src.core.cliente.application.use_case.actions.deactivate_cliente import DeactivateCliente
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.infra.in_memory_cliente_repository import InMemoryClienteRepository


class TestDeactivateClienteIntegration(TestCase):
    def setUp(self):
        self.repository = InMemoryClienteRepository()
        self.cliente = Cliente(nome="João Silva", email="joao.silva@example.com", is_active=True)
        self.repository.save(self.cliente)
        self.use_case = DeactivateCliente(repository=self.repository)

    def test_deactivate_cliente(self):
        self.use_case.execute(cliente_id=self.cliente.id, alterado_por="Admin")

        cliente_desativado = self.repository.get_by_id(self.cliente.id)
        self.assertFalse(cliente_desativado.is_active)
