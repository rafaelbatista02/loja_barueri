from django.shortcuts import render
from vendas.serializers import VendaSerializer
from vendas.models import Venda
from rest_framework import viewsets
# Create your views here.

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer