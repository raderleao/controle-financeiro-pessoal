
from unittest.mock import create_autospec
from uuid import uuid4
import uuid

import pytest
from src.core.cliente.application.repository.cliente_repository import ClienteRepository
from src.core.cliente.application.use_case.delete_cliente import DeleteCliente, DeleteClienteRequest
from src.core.cliente.domain.exceptions import ClienteNotFound
from src.core.cliente.domain.cliente import Cliente


class TestDeleteCliente:
    def test_delete_cliente_from_repository(self):
        cliente = Cliente(
            nome="Ráder",
            email="exemplo@example.com",
        )
        mock_repository = create_autospec(ClienteRepository)
        mock_repository.get_by_id.return_value = cliente

        use_case = DeleteCliente(mock_repository)
        use_case.execute(DeleteClienteRequest(id=cliente.id))

        mock_repository.delete.assert_called_once_with(cliente.id)

    def test_when_cliente_not_found_then_raise_exception(self):
        mock_repository  = create_autospec(ClienteRepository)
        mock_repository.get_by_id.return_value = None

        use_case = DeleteCliente(mock_repository)

        with pytest.raises(ClienteNotFound):
            use_case.execute(DeleteClienteRequest(id=uuid.uuid4()))

        mock_repository.delete.assert_not_called

