from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.request import Request
from .models import Cliente
from .serializers import ClienteSerializer


class ClienteViewSet(viewsets.ViewSet):
    """
    ViewSet para gerenciar clientes.
    """

    def list(self, request: Request) -> Response:
        """
        Retorna todos os clientes do banco de dados.
        """
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(status=HTTP_200_OK, data=serializer.data)

    def create(self, request: Request) -> Response:
        """
        Cria um novo cliente.
        """
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_201_CREATED, data=serializer.data)
        return Response(status=400, data=serializer.errors)

    def retrieve(self, request: Request, pk=None) -> Response:
        """
        Retorna um cliente específico pelo ID.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
            serializer = ClienteSerializer(cliente)
            return Response(status=HTTP_200_OK, data=serializer.data)
        except Cliente.DoesNotExist:
            return Response(status=404, data={"detail": "Cliente não encontrado."})

    def update(self, request: Request, pk=None) -> Response:
        """
        Atualiza um cliente específico pelo ID.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
            serializer = ClienteSerializer(cliente, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=HTTP_200_OK, data=serializer.data)
            return Response(status=400, data=serializer.errors)
        except Cliente.DoesNotExist:
            return Response(status=404, data={"detail": "Cliente não encontrado."})

    def destroy(self, request: Request, pk=None) -> Response:
        """
        Deleta um cliente específico pelo ID.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
            cliente.delete()
            return Response(status=HTTP_204_NO_CONTENT)
        except Cliente.DoesNotExist:
            return Response(status=404, data={"detail": "Cliente não encontrado."})
