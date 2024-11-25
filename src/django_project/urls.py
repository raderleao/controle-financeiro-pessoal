from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django_project.cliente_app.views import ClienteViewSet

# Configuração do roteador
router = DefaultRouter()
router.register(r"clientes", ClienteViewSet, basename="cliente")  # "api/" removido daqui

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o admin
    path('api/', include(router.urls)),  # Inclui as rotas do DRF com o namespace "api/"
]
