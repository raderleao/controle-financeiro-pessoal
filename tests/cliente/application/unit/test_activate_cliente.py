from unittest import TestCase
from unittest.mock import create_autospec
import uuid

from src.core.cliente.application.repository.cliente_repository import ClienteRepository
from src.core.cliente.application.use_case.actions.activate_cliente import ActivateCliente
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.domain.exceptions import ClienteNotFound


class TestActivateCliente(TestCase):
    def setUp(self):
        self.mock_repository = create_autospec(ClienteRepository)
        self.cliente = Cliente(nome="João Silva", email="joao.silva@example.com", is_active=False)
        self.mock_repository.get_by_id.return_value = self.cliente
        self.use_case = ActivateCliente(repository=self.mock_repository)

    def test_activate_cliente(self):
        self.use_case.execute(cliente_id=self.cliente.id, alterado_por="Admin")

        self.assertTrue(self.cliente.is_active)
        self.mock_repository.save.assert_called_once_with(self.cliente)

    def test_activate_cliente_not_found(self):
        self.mock_repository.get_by_id.return_value = None

        with self.assertRaises(ClienteNotFound):
            self.use_case.execute(cliente_id=uuid.uuid4(), alterado_por="Admin")
