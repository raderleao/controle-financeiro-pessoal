import pytest
from core.cliente.domain.cliente import Cliente as DomainCliente
from django_project.cliente_app.models import Cliente as ORMCliente
from django_project.cliente_app.repository import DjangoORMClienteRepository
import uuid
from datetime import datetime

@pytest.fixture
def cliente_repository():
    """Cria uma instância do repositório."""
    return DjangoORMClienteRepository()

@pytest.fixture
def cliente_dominio():
    """Cria um objeto do domínio."""
    return DomainCliente(
        id=uuid.uuid4(),
        nome="Cliente Teste",
        email="teste@email.com",
        is_active=True,
        criado_por="Admin",
        atualizado_por="Admin",
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now(),
        historico_alteracoes=[]
    )

@pytest.mark.django_db
def test_save_cliente(cliente_repository, cliente_dominio):
    """Testa o método save do repositório."""
    cliente_repository.save(cliente_dominio)
    orm_cliente = ORMCliente.objects.get(id=cliente_dominio.id)
    assert orm_cliente.nome == cliente_dominio.nome
    assert orm_cliente.email == cliente_dominio.email

@pytest.mark.django_db
def test_find_by_id(cliente_repository, cliente_dominio):
    """Testa o método find_by_id do repositório."""
    ORMCliente.objects.create(
        id=cliente_dominio.id,
        nome=cliente_dominio.nome,
        email=cliente_dominio.email,
        is_active=cliente_dominio.is_active,
        criado_por=cliente_dominio.criado_por,
        atualizado_por=cliente_dominio.atualizado_por,
        data_criacao=cliente_dominio.data_criacao,
        data_atualizacao=cliente_dominio.data_atualizacao,
        historico_alteracoes=cliente_dominio.historico_alteracoes
    )
    cliente = cliente_repository.find_by_id(cliente_dominio.id)
    assert cliente.nome == cliente_dominio.nome

@pytest.mark.django_db
def test_find_all(cliente_repository, cliente_dominio):
    """Testa o método find_all do repositório."""
    ORMCliente.objects.create(
        id=cliente_dominio.id,
        nome=cliente_dominio.nome,
        email=cliente_dominio.email,
        is_active=cliente_dominio.is_active,
        criado_por=cliente_dominio.criado_por,
        atualizado_por=cliente_dominio.atualizado_por,
        data_criacao=cliente_dominio.data_criacao,
        data_atualizacao=cliente_dominio.data_atualizacao,
        historico_alteracoes=cliente_dominio.historico_alteracoes
    )
    clientes = cliente_repository.find_all()
    assert len(clientes) == 1
    assert clientes[0].nome == cliente_dominio.nome

@pytest.mark.django_db
def test_delete_cliente(cliente_repository, cliente_dominio):
    """Testa o método delete do repositório."""
    ORMCliente.objects.create(
        id=cliente_dominio.id,
        nome=cliente_dominio.nome,
        email=cliente_dominio.email,
        is_active=cliente_dominio.is_active,
        criado_por=cliente_dominio.criado_por,
        atualizado_por=cliente_dominio.atualizado_por,
        data_criacao=cliente_dominio.data_criacao,
        data_atualizacao=cliente_dominio.data_atualizacao,
        historico_alteracoes=cliente_dominio.historico_alteracoes
    )
    result = cliente_repository.delete(cliente_dominio.id)
    assert result is True
    assert not ORMCliente.objects.filter(id=cliente_dominio.id).exists()
