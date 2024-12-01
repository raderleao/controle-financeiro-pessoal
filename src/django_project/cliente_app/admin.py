from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'is_active', 'data_criacao', 'data_atualizacao')
    list_filter = ('is_active', 'data_criacao')
    search_fields = ('nome', 'email')
    ordering = ('-data_criacao',)
    readonly_fields = ('id', 'data_criacao', 'data_atualizacao', 'historico_alteracoes')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('id', 'nome', 'email', 'is_active')
        }),
        ('Registro e Atualização', {
            'fields': ('criado_por', 'atualizado_por', 'data_criacao', 'data_atualizacao', 'historico_alteracoes')
        }),
    )

