from datetime import datetime
from uuid import UUID
import uuid

import pytest
from src.core.cliente.application.use_case.get_cliente import GetCliente, GetClienteRequest, GetClienteResponse
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.infra.in_memory_cliente_repository import InMemoryClienteRepository
from src.core.cliente.domain.exceptions import ClienteNotFound

class TestGetCliente:
    def test_get_cliente_by_id(self):
        cliente1 = Cliente(
            nome="Ráder",
            email="email@example.com",
            is_active=True,
            criado_por="Admin",
            atualizado_por="Admin",
            data_criacao=datetime(2023, 1, 1, 12, 0),
            data_atualizacao=datetime(2023, 1, 1, 12, 0)
        )
        cliente2 = Cliente(
            nome="Bruna",
            email="brunaeverton@live.com",
            is_active=True,
            criado_por="Admin",
            atualizado_por="Admin",
            data_criacao=datetime(2023, 1, 2, 12, 0),
            data_atualizacao=datetime(2023, 1, 2, 12, 0),
        )

        repository = InMemoryClienteRepository(
            clientes=[cliente1, cliente2]
        )

        use_case = GetCliente(repository=repository)
        request = GetClienteRequest(
            id=cliente1.id
        )

        response = use_case.execute(request)

        assert response == GetClienteResponse(
            id=cliente1.id,
            nome="Ráder",
            email="email@example.com",
            is_active=True,
            criado_por="Admin",
            atualizado_por="Admin",
            data_criacao=datetime(2023, 1, 1, 12, 0),
            data_atualizacao=datetime(2023, 1, 1, 12, 0),
        )

    def test_when_cliente_does_not_exist_then_raise_exception(self):
        cliente1 = Cliente(
            nome="Ráder",
            email="email@example.com",
            is_active=True,
            criado_por="Admin",
            atualizado_por="Admin",
            data_criacao=datetime(2023, 1, 1, 12, 0),
            data_atualizacao=datetime(2023, 1, 1, 12, 0)
        )
        cliente2 = Cliente(
            nome="Bruna",
            email="brunaeverton@live.com",
            is_active=True,
            criado_por="Admin",
            atualizado_por="Admin",
            data_criacao=datetime(2023, 1, 2, 12, 0),
            data_atualizacao=datetime(2023, 1, 2, 12, 0),
        )

        repository = InMemoryClienteRepository(
            clientes=[cliente1, cliente2]
        )

        use_case = GetCliente(repository=repository)
        not_found_id = uuid.uuid4()

        request = GetClienteRequest(
            id=not_found_id
        )

        with pytest.raises(ClienteNotFound) as exc:
                use_case.execute(request)
        

    