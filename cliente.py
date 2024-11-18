import uuid
from datetime import datetime

class Cliente:
    def __init__(self, id=None, nome='', email='', is_active=True, criado_por=None, atualizado_por=None):
        
        self.id = id or uuid.uuid4()
        self.nome = nome
        self.email = email
        self.is_active = is_active
        self.data_criacao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.criado_por = criado_por
        self.atualizado_por = atualizado_por
        self.validate()

    def validate(self):
        
        if len(self.nome) > 255:
            raise ValueError("nome cannot be longer than 255")
        
        if not self.nome:
            raise ValueError("nome cannot be empty")

    def __str__(self):
        return f"{self.nome} - {self.email} ({self.is_active})"
    
    def __repr__(self):
        return f"<Cliente {self.nome} - {self.email}>"
    
    def update_cliente(self, nome, email):
        self.nome = nome
        self.email = email

        self.validate()

    def activate(self):
        self.is_active = True

        self.validate()

    def deactivate(self):
        self.is_active = not self.is_active 
        self.validate()
    