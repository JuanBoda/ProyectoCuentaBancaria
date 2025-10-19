from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import cliente_service


@login_required
def lista_cliente(request):
    """
    Orquesta la obtención de la lista de clientes y la renderiza.
    Delega toda la lógica de negocio al servicio de clientes.
    """
    clientes = cliente_service.obtener_clientes_unificados()
    return render(request, "gestion_clientes/lista.html", {"clientes": clientes})
