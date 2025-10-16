from django.urls import path
from . views import lista_cliente

app_name = 'gestion_clientes'

urlpatterns = [
    path('', lista_cliente, name='lista'),
]
