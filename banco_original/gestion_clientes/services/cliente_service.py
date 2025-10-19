from ..models import PersonaFisica, PersonaJuridica
from django.db.models import Value, CharField
from itertools import chain


def obtener_clientes_unificados():
    """
    Obtiene una lista unificada de Personas Físicas y Jurídicas.
    Si no hay clientes, devuelve una lista de ejemplo.
    """
    pf = (
        PersonaFisica.objects.order_by("nombre")
        .values("id", "nombre", "dni", "cuil", "mail", "telefono", "direccion")
        .annotate(tipo=Value("Persona Física", output_field=CharField()))
    )
    pj = (
        PersonaJuridica.objects.order_by("razon_social")
        .values("id", "nombre", "cuil", "razon_social", "mail", "telefono", "direccion")
        .annotate(tipo=Value("Persona Jurídica", output_field=CharField()))
    )

    salida = list(chain(pf, pj))

    if not salida:
        salida = [
            {
                "tipo": "Persona Física",
                "nombre": "ANA LOPEZ",
                "cuil": "20123456783",
                "mail": "ana@ej.com",
                "telefono": "11133334444",
            },
            {
                "tipo": "Persona Jurídica",
                "nombre": "ACME S.A",
                "cuil": "30765432109",
                "mail": "info@acme.com",
                "telefono": "11144445555",
            },
        ]

    return salida