import pytest
from rest_framework.test import APIClient
from django_project.cliente_app.models import Cliente
import uuid

@pytest.fixture
def api_client():
    """Fixture para criar um cliente de teste para a API."""
    return APIClient()

@pytest.fixture
def cliente_teste(db):
    """Cria um cliente de teste no banco."""
    return Cliente.objects.create(
        id=uuid.uuid4(),
        nome="Cliente Teste",
        email="teste@email.com",
        is_active=True
    )

@pytest.mark.django_db
def test_lista_clientes(api_client, cliente_teste):
    """Testa o endpoint para listar todos os clientes."""
    response = api_client.get('/clientes/')
    assert response.status_code == 200
    assert len(response.data) > 0
    assert response.data[0]['nome'] == cliente_teste.nome

@pytest.mark.django_db
def test_criar_cliente(api_client):
    """Testa o endpoint para criar um cliente."""
    data = {
        "nome": "Novo Cliente",
        "email": "novo@email.com",
        "is_active": True
    }
    response = api_client.post('/clientes/', data=data, format='json')
    assert response.status_code == 201
    assert Cliente.objects.filter(nome="Novo Cliente").exists()

@pytest.mark.django_db
def test_atualizar_cliente(api_client, cliente_teste):
    """Testa o endpoint para atualizar um cliente."""
    data = {"nome": "Cliente Atualizado"}
    response = api_client.put(f'/clientes/{cliente_teste.id}/', data=data, format='json')
    assert response.status_code == 200
    cliente_teste.refresh_from_db()
    assert cliente_teste.nome == "Cliente Atualizado"

@pytest.mark.django_db
def test_deletar_cliente(api_client, cliente_teste):
    """Testa o endpoint para deletar um cliente."""
    response = api_client.delete(f'/clientes/{cliente_teste.id}/')
    assert response.status_code == 204
    assert not Cliente.objects.filter(id=cliente_teste.id).exists()
