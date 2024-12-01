from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django_project.cliente_app.views import ClienteViewSet

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet, basename="cliente")

urlpatterns = [
    path("admin/", admin.site.urls),
] + router.urls
