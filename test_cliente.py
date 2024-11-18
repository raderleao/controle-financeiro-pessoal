import pytest
from uuid import UUID
import uuid 

from cliente import Cliente

class TestCliente:
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

    def test_cliente_is_created_as_active_by_defefault(self):
        cliente = Cliente(nome="Ráder")
        assert cliente.is_active is True

    def test_cliente_is_created_with_provided_values(self):
        cli_id = uuid.uuid4()
        cliente = Cliente(
            id=cli_id,
            nome="Ráder",
            email="raderleao@hotmail.com",
            is_active=False,
            criado_por = "Pedro",
            atualizado_por="Joao"
        )
        assert cliente.id == cli_id
        assert cliente.nome == "Ráder"
        assert cliente.email == "raderleao@hotmail.com"
        assert cliente.is_active is False
        assert cliente.criado_por == "Pedro"
        assert cliente.atualizado_por == "Joao"

    def test_cannot_create_cliente_with_empity_nome(self):
        with pytest.raises(ValueError, match="nome cannot be empty"):
            Cliente(nome="")
        
class TestUpdateCliente:
    def test_update_cliente_with_nome_and_email(self):
        cliente = Cliente(nome="Ráder", email="raderleao@hotmail.com")

        cliente.update_cliente(nome="Bruna", email="brunaeverton@live.com")

        assert cliente.nome == "Bruna"
        assert cliente.email == "brunaeverton@live.com"

    def test_update_cliente_with_invalid_nome(self):
        cliente = Cliente(nome="Ráder", email="raderleao@hotmail.com")
        
        with pytest.raises(ValueError, match="nome cannot be longer than 255"):
            cliente.update_cliente(nome="a" * 256, email="brunaeverton@live.com")

    def test_cannot_update_cliente_with_empty_nome(self):
        with pytest.raises(ValueError, match="nome cannot be empty"):
            Cliente(nome="")


class TestActivate:
    def test_activzte_cliente(self):
        cliente = Cliente(
            nome="Ráder", 
            email="rader@example.com",
            is_active=False
        )

        cliente.activate()

        assert cliente.is_active is True

    def test_activate_active_cliente(self):
        cliente = Cliente(
            nome="Ráder", 
            email="rader@example.com",
            is_active=True
        )

        cliente.activate()

        assert cliente.is_active is True

    def test_deactivate_cliente(self):
        cliente = Cliente(
            nome="Ráder",
            email="rader@example.com",
            is_active=True  # Começa como ativo
        )

        cliente.deactivate()  # Chama o método `deactivate`

        assert cliente.is_active is False 