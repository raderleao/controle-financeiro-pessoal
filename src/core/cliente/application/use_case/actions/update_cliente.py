import re
from typing import Optional
from dataclasses import dataclass
import uuid
from datetime import datetime
from src.core.cliente.domain.cliente import Cliente
from src.core.cliente.domain.exceptions import ClienteNotFound, InvalidCliente

class UpdateCliente:
    @dataclass
    class Request:
        id: uuid.UUID
        nome: Optional[str] = None
        email: Optional[str] = None
        alterado_por: Optional[str] = None

    @dataclass
    class Response:
        id: uuid.UUID
        nome: str
        email: str
        is_active: bool
        data_criacao: datetime
        data_atualizacao: datetime
        historico_alteracoes: list

        @classmethod
        def from_cliente(cls, cliente: Cliente):
            return cls(
                id=cliente.id,
                nome=cliente.nome,
                email=cliente.email,
                is_active=cliente.is_active,
                data_criacao=cliente.data_criacao,
                data_atualizacao=cliente.data_atualizacao,
                historico_alteracoes=cliente.historico_alteracoes,
            )

    def __init__(self, repository):
        self.repository = repository

    def execute(self, request: "UpdateCliente.Request") -> "UpdateCliente.Response":

        # Busca o cliente no repositório
        cliente = self.repository.get_by_id(request.id)
        if not cliente:
            raise ClienteNotFound(request.id)

        # Valida os campos antes de alterar
        if request.nome is not None:
            self._validate_nome(request.nome)
        if request.email is not None:
            self._validate_email(request.email)

        # Atualiza os campos e registra histórico
        if request.nome is not None and request.nome != cliente.nome:
            cliente.historico_alteracoes.append({
                "campo": "nome",
                "anterior": cliente.nome,
                "novo": request.nome,
                "data_alteracao": datetime.now(),
                "alterado_por": request.alterado_por,
            })
            cliente.nome = request.nome

        if request.email is not None and request.email != cliente.email:
            cliente.historico_alteracoes.append({
                "campo": "email",
                "anterior": cliente.email,
                "novo": request.email,
                "data_alteracao": datetime.now(),
                "alterado_por": request.alterado_por,
            })
            cliente.email = request.email

        cliente.data_atualizacao = datetime.now()

        # Salva o cliente atualizado
        self.repository.save(cliente)

        return self.Response.from_cliente(cliente)

    def _validate_nome(self, nome: str):
        """Valida o campo nome."""
        if nome.strip() == "":
            raise InvalidCliente("nome cannot be empty")
        if len(nome) > 255:
            raise ValueError("nome cannot be longer than 255")

    def _validate_email(self, email: str):
        """Valida o formato do email."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise InvalidCliente("Invalid email format")


    def _get_cliente(self, cliente_id: uuid.UUID) -> Cliente:
        """
        Recupera o cliente do repositório. Lança ClienteNotFound se não existir.
        """
        cliente = self.repository.get_by_id(cliente_id)
        if not cliente:
            raise ClienteNotFound(cliente_id)
        return cliente

    def _update_nome(self, cliente: Cliente, novo_nome: Optional[str], alterado_por: Optional[str]):
        """
        Atualiza o nome do cliente, se necessário.
        """
        if novo_nome and novo_nome != cliente.nome:
            if novo_nome == "":
                raise ValueError("nome cannot be empty")
            if len(novo_nome) > 255:
                raise ValueError("nome cannot be longer than 255")
            cliente.historico_alteracoes.append({
                "campo": "nome",
                "anterior": cliente.nome,
                "novo": novo_nome,
                "data_alteracao": datetime.now(),
                "alterado_por": alterado_por,
            })
            cliente.nome = novo_nome

    def _update_email(self, cliente: Cliente, novo_email: Optional[str], alterado_por: Optional[str]):
        """
        Atualiza o email do cliente, se necessário.
        """
        if novo_email and novo_email != cliente.email:
            cliente.historico_alteracoes.append({
                "campo": "email",
                "anterior": cliente.email,
                "novo": novo_email,
                "data_alteracao": datetime.now(),
                "alterado_por": alterado_por,
            })
            cliente.email = novo_email
