from unittest import TestCase
from unittest.mock import create_autospec

import pytest
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.application.use_case.actions.update_cliente import UpdateCliente
from src.core.cliente.domain.repository.cliente_repository import ClienteRepository
import uuid

from src.core.cliente.domain.exceptions import ClienteNotFound

class TestUpdateCliente(TestCase):
    def setUp(self):
        self.mock_repository = create_autospec(ClienteRepository)
        self.cliente = Cliente(nome="João Silva", email="joao.silva@example.com")
        self.mock_repository.get_by_id.return_value = self.cliente
        self.use_case = UpdateCliente(repository=self.mock_repository)

    def test_update_cliente_nome(self):
        request = UpdateCliente.Request(id=self.cliente.id, nome="João Carlos")
        self.use_case.execute(request)

        self.assertEqual(self.cliente.nome, "João Carlos")
        self.mock_repository.save.assert_called_once_with(self.cliente)

    def test_update_cliente_email(self):
        request = UpdateCliente.Request(id=self.cliente.id, email="joao.carlos@example.com")
        self.use_case.execute(request)

        self.assertEqual(self.cliente.email, "joao.carlos@example.com")
        self.mock_repository.save.assert_called_once_with(self.cliente)

    def test_update_cliente_not_found(self):
        """Testa a tentativa de atualizar um cliente que não existe."""
        # Configuração: Retorna None ao buscar cliente inexistente
        self.mock_repository.get_by_id.return_value = None

        # Request para atualizar cliente
        request = UpdateCliente.Request(id=uuid.uuid4(), nome="Novo Nome")

        # Verifica se a exceção correta é levantada
        with pytest.raises(ClienteNotFound) as exc_info:
            self.use_case.execute(request)

        # Valida se o ID do cliente ausente está na mensagem da exceção
        assert str(request.id) in str(exc_info.value)
