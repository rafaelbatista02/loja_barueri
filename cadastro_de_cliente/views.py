from django.shortcuts import render
from rest_framework import viewsets
from cadastro_de_cliente.models import Clientes
from cadastro_de_cliente.serializers import ClientesSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

# Create your views here.
