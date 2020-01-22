from rest_framework import routers
from produtos.views import ProdutoViewSet
from django.contrib import admin
from vendas.views import VendaViewSet
from django.urls import path, include
from cadastro_de_cliente.views import ClientesViewSet
  

rota = routers.DefaultRouter()
rota.register(r'produtos', ProdutoViewSet)
rota.register(r'vendas', VendaViewSet)
rota.register(r'clientes',ClientesViewSet)


urlpatterns = [
    path(r'cliente/', include(rota.urls)),
    path(r'api/', include(rota.urls)),
    path('admin/', admin.site.urls),
]
