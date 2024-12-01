import pytest
from unittest import TestCase
from unittest.mock import create_autospec
from uuid import UUID
import uuid
from src.core.cliente.application.use_case.actions.update_cliente import UpdateCliente
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.domain.repository.cliente_repository import ClienteRepository
from src.core.cliente.domain.exceptions import InvalidCliente


class BaseTestCliente(TestCase):
    """
    Classe base para os testes relacionados ao cliente.
    """
    def setUp(self):
        """
        Configura os objetos necessários para os testes.
        """
        self.mock_repository = create_autospec(ClienteRepository)
        self.cliente = Cliente(nome="Ráder", email="raderleao@hotmail.com")
        self.mock_repository.get_by_id.return_value = self.cliente
        self.use_case = UpdateCliente(repository=self.mock_repository)


class TestCliente(BaseTestCliente):
    def test_nome_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'nome'"):
            Cliente()

    def test_nome_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="nome cannot be longer than 255"):
            Cliente(nome="a" * 256)

    def test_cliente_must_be_created_with_id_as_uuid_by_default(self):
        cliente = Cliente(nome="Ráder")
        assert isinstance(cliente.id, UUID)

    def test_created_cliente_with_default_values(self):
        cliente = Cliente(nome="Ráder")
        assert cliente.nome == "Ráder"
        assert cliente.email == ""
        assert cliente.is_active is True

    def test_cannot_create_cliente_with_empty_nome(self):
        with pytest.raises(ValueError, match="nome cannot be empty"):
            Cliente(nome="")

    def test_str_representation(self):
        cliente = Cliente(nome="Ráder", email="rader@example.com")
        assert str(cliente) == "Ráder - rader@example.com (Ativo)"

    def test_repr_representation(self):
        cliente = Cliente(nome="Ráder", email="rader@example.com")
        assert repr(cliente) == "<Cliente Ráder - rader@example.com>"


class TestUpdateCliente(BaseTestCliente):
    def test_update_cliente_with_nome_and_email(self):
        request = UpdateCliente.Request(
            id=self.cliente.id,
            nome="Bruna",
            email="brunaeverton@live.com",
            alterado_por="Admin"
        )
        response = self.use_case.execute(request)

        # Verifica os valores atualizados
        self.assertEqual(response.nome, "Bruna")
        self.assertEqual(response.email, "brunaeverton@live.com")

        # Verifica o histórico de alterações
        self.assertEqual(len(response.historico_alteracoes), 2)
        self.assertEqual(response.historico_alteracoes[0]["campo"], "nome")
        self.assertEqual(response.historico_alteracoes[1]["campo"], "email")

        # Verifica se o cliente foi salvo no repositório
        self.mock_repository.save.assert_called_once_with(self.cliente)

    def test_update_cliente_with_invalid_nome(self):
        # Configurando a solicitação
        request = UpdateCliente.Request(
            id=self.cliente.id,
            nome="a" * 256,  # Nome inválido
            email="brunaeverton@live.com",
            alterado_por="Admin"
        )

        # Verifica se a exceção é levantada ao tentar atualizar com nome inválido
        with pytest.raises(ValueError, match="nome cannot be longer than 255"):
            self.use_case.execute(request)
            
    def test_cannot_update_cliente_with_empty_nome(self):
        # Configurando a solicitação com nome vazio
        request = UpdateCliente.Request(
            id=self.cliente.id,
            nome="",  # Nome vazio
            email="brunaeverton@live.com",
            alterado_por="Admin"
        )

        # Verifica se a exceção é levantada ao tentar atualizar com nome vazio
        with pytest.raises(InvalidCliente, match="nome cannot be empty"):
            self.use_case.execute(request)

class TestActivate(BaseTestCliente):
    def test_activate_cliente(self):
        self.cliente.is_active = False
        self.cliente.activate(alterado_por="Admin")
        assert self.cliente.is_active is True

    def test_activate_active_cliente(self):
        self.cliente.is_active = True
        self.cliente.activate(alterado_por="Admin")
        assert self.cliente.is_active is True

    def test_deactivate_cliente(self):
        self.cliente.is_active = True
        self.cliente.deactivate(alterado_por="Admin")
        assert self.cliente.is_active is False


class TestEquality(BaseTestCliente):
    def test_when_clientes_have_same_id_they_are_equal(self):
        common_id = uuid.uuid4()
        cliente_1 = Cliente(nome="Rayssa", id=common_id)
        cliente_2 = Cliente(nome="Rayssa", id=common_id)
        assert cliente_1 == cliente_2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id = uuid.uuid4()
        cliente = Cliente(nome="Rayssa", id=common_id)
        dummy = Dummy()
        dummy.id = common_id
        assert cliente != dummy
