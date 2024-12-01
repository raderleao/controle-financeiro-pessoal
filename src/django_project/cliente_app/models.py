from django.db import models
import uuid

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    criado_por = models.CharField(max_length=255, null=True, blank=True, default='AdminA')
    atualizado_por = models.CharField(max_length=255, null=True, blank=True, default='AdminA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    historico_alteracoes = models.JSONField(default=list)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-data_criacao"]
        db_table = "cliente"

    def __str__(self):
        return f"{self.nome} - {self.email} ({'Ativo' if self.is_active else 'Inativo'})"
