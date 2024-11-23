from unittest.mock import MagicMock, create_autospec
from src.core.cliente.application.repository.cliente_repository import ClienteRepository
from src.core.cliente.application.use_case.get_cliente import GetCliente, GetClienteRequest, GetClienteResponse
from src.core.cliente.domain.cliente import Cliente

class TestGetCliente:
    def test_return_found_cliente(self):
        cliente = Cliente(
            nome="Ráder",
            email="email@example.com",
            is_active=True,
            criado_por="Administrador",
            atualizado_por="Administrador"

        )
        mock_repository = create_autospec(ClienteRepository)
        mock_repository.get_by_id.return_value = cliente

        use_case = GetCliente(repository=mock_repository)
        request = GetClienteRequest(
            id=cliente.id,
        )

        response = use_case.execute(request)

        assert response == GetClienteResponse(
            id=cliente.id,
            nome="Ráder",
            email="email@example.com",
            is_active=True,
            criado_por="Administrador",
            atualizado_por="Administrador",
            data_criacao=cliente.data_criacao,
            data_atualizacao=cliente.data_atualizacao
        )
        mock_repository.get_by_id.assert_called_once_with(cliente.id)