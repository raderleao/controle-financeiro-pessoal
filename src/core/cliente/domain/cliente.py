from dataclasses import dataclass, field
import uuid
from datetime import datetime


@dataclass
class Cliente:
    nome: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    email: str = field(default='')
    is_active: bool = field(default=True)
    criado_por: str = field(default=None)
    atualizado_por: str = field(default=None)
    data_criacao: datetime = field(default_factory=datetime.now)
    data_atualizacao: datetime = field(default_factory=datetime.now)
    historico_alteracoes: list = field(default_factory=list)  # Armazena histórico de alterações

    def __post_init__(self):
        """Valida o cliente imediatamente após a inicialização."""
        self.validate()

    def validate(self):
        """Valida os dados do cliente."""
        if not self.nome:
            raise ValueError("nome cannot be empty")
        if len(self.nome) > 255:
            raise ValueError("nome cannot be longer than 255 characters")
        self.validate_email()

    def validate_email(self):
        """Valida o formato do email."""
        if self.email and "@" not in self.email:
            raise ValueError("Invalid email format")

    def __str__(self):
        """Representação amigável do cliente."""
        return f"{self.nome} - {self.email} ({'Ativo' if self.is_active else 'Inativo'})"

    def __repr__(self):
        """Representação técnica do cliente."""
        return f"<Cliente {self.nome} - {self.email}>"

    def __eq__(self, other):
        """Compara clientes com base no ID."""
        if not isinstance(other, Cliente):
            return False
        return self.id == other.id

    def update_data(self, campo: str, novo_valor: str, alterado_por: str):
        """Atualiza o campo especificado e registra no histórico."""
        valor_anterior = getattr(self, campo)
        if valor_anterior != novo_valor:
            self.historico_alteracoes.append({
                "campo": campo,
                "anterior": valor_anterior,
                "novo": novo_valor,
                "data_alteracao": datetime.now(),
                "alterado_por": alterado_por
            })
            setattr(self, campo, novo_valor)
            self.data_atualizacao = datetime.now()
            self.atualizado_por = alterado_por

    def activate(self, alterado_por: str):
        """Ativa o cliente e registra no histórico."""
        if not self.is_active:
            self.historico_alteracoes.append({
                "campo": "is_active",
                "anterior": False,
                "novo": True,
                "data_alteracao": datetime.now(),
                "alterado_por": alterado_por,
            })
            self.is_active = True
            self.data_atualizacao = datetime.now()
            self.atualizado_por = alterado_por

    def deactivate(self, alterado_por: str):
        """Desativa o cliente e registra no histórico."""
        if self.is_active:
            self.historico_alteracoes.append({
                "campo": "is_active",
                "anterior": True,
                "novo": False,
                "data_alteracao": datetime.now(),
                "alterado_por": alterado_por,
            })
            self.is_active = False
            self.data_atualizacao = datetime.now()
            self.atualizado_por = alterado_por
