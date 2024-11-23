import pytest
from unittest.mock import Mock
from src.core.cliente.application.use_case.list_cliente import ListCliente, ListClienteRequest
from src.core.cliente.domain.cliente import Cliente
from datetime import datetime
from uuid import uuid4

@pytest.fixture
def mock_repositorio():
    """Mock do repositório de clientes."""
    repositorio = Mock()
    repositorio.list = Mock()
    return repositorio

def test_listar_todos_os_clientes(mock_repositorio):
    # Simula clientes no repositório
    clientes = [
        Cliente(
            id=str(uuid4()),
            nome="João",
            email="joao@example.com",
            is_active=True,
            criado_por="admin",
            atualizado_por="admin",
            data_criacao=datetime.now(),
            data_atualizacao=datetime.now(),
            historico_alteracoes=[]
        ),
        Cliente(
            id=str(uuid4()),
            nome="Maria",
            email="maria@example.com",
            is_active=False,
            criado_por="admin",
            atualizado_por="admin",
            data_criacao=datetime.now(),
            data_atualizacao=datetime.now(),
            historico_alteracoes=[]
        )
    ]
    mock_repositorio.list.return_value = clientes

    # Caso de uso
    use_case = ListCliente(mock_repositorio)
    request = ListClienteRequest()
    response = use_case.execute(request)

    # Validações
    assert len(response.data) == 2
    assert response.data[0].nome == "João"
    assert response.data[1].nome == "Maria"
    mock_repositorio.list.assert_called_once_with(ativos=None)

def test_listar_apenas_clientes_ativos(mock_repositorio):
    # Simula clientes no repositório
    clientes = [
        Cliente(
            id=str(uuid4()),
            nome="João",
            email="joao@example.com",
            is_active=True,
            criado_por="admin",
            atualizado_por="admin",
            data_criacao=datetime.now(),
            data_atualizacao=datetime.now(),
            historico_alteracoes=[]
        )
    ]
    mock_repositorio.list.return_value = clientes

    # Caso de uso
    use_case = ListCliente(mock_repositorio)
    request = ListClienteRequest(ativos=True)
    response = use_case.execute(request)

    # Validações
    assert len(response.data) == 1
    assert response.data[0].nome == "João"
    assert response.data[0].is_active is True
    mock_repositorio.list.assert_called_once_with(ativos=True)
