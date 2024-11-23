import pytest
from datetime import datetime
from uuid import uuid4
from src.core.cliente.application.use_case.list_cliente import ListCliente, ListClienteRequest
from src.core.cliente.infra.in_memory_cliente_repository import InMemoryClienteRepository
from src.core.cliente.domain.cliente import Cliente

@pytest.fixture
def repositorio_cliente():
    """Repositório em memória para integração."""
    return InMemoryClienteRepository()

def test_listar_todos_os_clientes(repositorio_cliente):
    # Adicionar clientes ao repositório
    repositorio_cliente.save(Cliente(
        id=str(uuid4()),
        nome="João",
        email="joao@example.com",
        is_active=True,
        criado_por="admin",
        atualizado_por="admin",
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now(),
        historico_alteracoes=[]
    ))
    repositorio_cliente.save(Cliente(
        id=str(uuid4()),
        nome="Maria",
        email="maria@example.com",
        is_active=False,
        criado_por="admin",
        atualizado_por="admin",
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now(),
        historico_alteracoes=[]
    ))

    # Caso de uso
    use_case = ListCliente(repositorio_cliente)
    request = ListClienteRequest()  # Request para listar todos
    resultado = use_case.execute(request)

    # Validações
    assert len(resultado.data) == 2
    assert resultado.data[0].nome == "João"
    assert resultado.data[1].nome == "Maria"

def test_listar_apenas_clientes_ativos(repositorio_cliente):
    # Adicionar clientes ao repositório
    repositorio_cliente.save(Cliente(
        id=str(uuid4()),
        nome="João",
        email="joao@example.com",
        is_active=True,
        criado_por="admin",
        atualizado_por="admin",
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now(),
        historico_alteracoes=[]
    ))
    repositorio_cliente.save(Cliente(
        id=str(uuid4()),
        nome="Maria",
        email="maria@example.com",
        is_active=False,
        criado_por="admin",
        atualizado_por="admin",
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now(),
        historico_alteracoes=[]
    ))

    # Caso de uso
    use_case = ListCliente(repositorio_cliente)
    request = ListClienteRequest(ativos=True)  # Request para listar apenas ativos
    resultado = use_case.execute(request)

    # Validações
    assert len(resultado.data) == 1
    assert resultado.data[0].nome == "João"
    assert resultado.data[0].is_active is True

def test_listar_apenas_clientes_inativos(repositorio_cliente):
    # Adicionar clientes ao repositório
    repositorio_cliente.save(Cliente(
        id=str(uuid4()),
        nome="João",
        email="joao@example.com",
        is_active=True,
        criado_por="admin",
        atualizado_por="admin",
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now(),
        historico_alteracoes=[]
    ))
    repositorio_cliente.save(Cliente(
        id=str(uuid4()),
        nome="Maria",
        email="maria@example.com",
        is_active=False,
        criado_por="admin",
        atualizado_por="admin",
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now(),
        historico_alteracoes=[]
    ))

    # Caso de uso
    use_case = ListCliente(repositorio_cliente)
    request = ListClienteRequest(ativos=False)  # Request para listar apenas inativos
    resultado = use_case.execute(request)

    # Validações
    assert len(resultado.data) == 1
    assert resultado.data[0].nome == "Maria"
    assert resultado.data[0].is_active is False

def test_listar_sem_clientes(repositorio_cliente):
    # Caso de uso
    use_case = ListCliente(repositorio_cliente)
    request = ListClienteRequest()  # Request para listar todos
    resultado = use_case.execute(request)

    # Validações
    assert len(resultado.data) == 0
