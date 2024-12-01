from core.cliente.domain.repository.cliente_repository import ClienteRepository
from src.core.cliente.domain.cliente import Cliente as DomainCliente
from django_project.cliente_app.models import Cliente as DefaultClienteModel


class DjangoORMClienteRepository(ClienteRepository):
    def __init__(self, cliente_model=DefaultClienteModel):
        """
        Inicializa o repositório com o modelo ORM.
        :param cliente_model: Modelo ORM usado pelo repositório (default: DefaultClienteModel).
        """
        self.cliente_model = cliente_model

    def save(self, cliente: DomainCliente):
        """Salva ou atualiza um cliente no banco de dados."""
        orm_cliente, created = self.cliente_model.objects.update_or_create(
            id=cliente.id,
            defaults={
                'nome': cliente.nome,
                'email': cliente.email,
                'is_active': cliente.is_active,
                'criado_por': cliente.criado_por,
                'atualizado_por': cliente.atualizado_por,
                'historico_alteracoes': cliente.historico_alteracoes,
                'data_criacao': cliente.data_criacao,
                'data_atualizacao': cliente.data_atualizacao,
            },
        )
        return self._to_domain(orm_cliente)

    def find_by_id(self, cliente_id):
        """Busca um cliente pelo ID."""
        try:
            orm_cliente = self.cliente_model.objects.get(id=cliente_id)
            return self._to_domain(orm_cliente)
        except self.cliente_model.DoesNotExist:
            return None

    def find_all(self):
        """Retorna todos os clientes."""
        orm_clientes = self.cliente_model.objects.all()
        return [self._to_domain(orm_cliente) for orm_cliente in orm_clientes]

    def delete(self, cliente_id):
        """Remove um cliente pelo ID."""
        try:
            orm_cliente = self.cliente_model.objects.get(id=cliente_id)
            orm_cliente.delete()
            return True
        except self.cliente_model.DoesNotExist:
            return False

    def get_by_id(self, cliente_id):
        """Implementação do método abstrato get_by_id."""
        return self.find_by_id(cliente_id)

    def list(self):
        """Implementação do método abstrato list."""
        return self.find_all()

    def _to_domain(self, orm_cliente) -> DomainCliente:
        """Converte um modelo ORM em um objeto do domínio."""
        return DomainCliente(
            id=orm_cliente.id,
            nome=orm_cliente.nome,
            email=orm_cliente.email,
            is_active=orm_cliente.is_active,
            criado_por=orm_cliente.criado_por,
            atualizado_por=orm_cliente.atualizado_por,
            historico_alteracoes=orm_cliente.historico_alteracoes,
            data_criacao=orm_cliente.data_criacao,
            data_atualizacao=orm_cliente.data_atualizacao,
        )
