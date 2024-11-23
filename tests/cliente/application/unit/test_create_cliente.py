from unittest.mock import MagicMock
import pytest
from uuid import UUID
from src.core.cliente.application.repository.cliente_repository import ClienteRepository
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.application.use_case.create_cliente import CreateCliente, CreateClienteRequest, CreateClienteResponse
from src.core.cliente.domain.exceptions import InvalidCliente

class TestCreateCliente:
    def test_create_cliente_with_valid_data(self):
        mock_repository = MagicMock(ClienteRepository)
        use_case = CreateCliente(repository=mock_repository)
        request = CreateClienteRequest(
            nome="Ráder",
            email="test@example.com",
            is_active=True,
            criado_por="Admin",
            atualizado_por="Admin"
        )

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response, CreateClienteResponse)
        assert isinstance(response.id, UUID)
        assert mock_repository.save.called is True

    def test_create_cliente_with_empty_nome_raises_error(self):
        mock_repository = MagicMock(ClienteRepository)
        use_case = CreateCliente(repository=mock_repository)

        with pytest.raises(InvalidCliente, match="nome cannot be empty"):
            request = CreateClienteRequest(
                nome="",  # Nome vazio
                email="test@example.com"
            )
            use_case.execute(request)

    def test_create_cliente_with_invalid_data(self):
        use_case = CreateCliente(repository=MagicMock(ClienteRepository))

        with pytest.raises(InvalidCliente, match="nome cannot be empty") as exc_info:
            use_case.execute(CreateClienteRequest(nome="", email="test@example.com"))

        # Valida o tipo da exceção levantada
        assert exc_info.type is InvalidCliente
        # Valida a mensagem da exceção
        assert str(exc_info.value) == "nome cannot be empty"

    def test_create_cliente_with_long_nome_raises_error(self):
        with pytest.raises(ValueError, match="nome cannot be longer than 255"):
            Cliente(nome="a" * 256)

    def test_create_cliente_generates_uuid_by_default(self):
        cliente = Cliente(nome="Ráder")
        assert isinstance(cliente.id, UUID)

    def test_create_cliente_with_default_values(self):
        cliente = Cliente(nome="Ráder")
        assert cliente.email == ""
        assert cliente.is_active is True
        assert cliente.criado_por is None
        assert cliente.atualizado_por is None
