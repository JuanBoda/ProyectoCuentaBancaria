from common.helpers import limpiar_texto, colapsar_espacios, solo_digitos

CARACTERES_NOMBRE = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "áéíóúüñÁÉÍÓÚÜÑ"
    "àèìòùÀÈÌÒÙ"
    "äëïöüÄËÏÖÜÑ"
    "ãõÃÕ"
    "çÇ"
    " -'."
    "\u00c1\u00c9\u00cd\u00d3\u00da\u00dc\u00d1"
    "\u00e1\u00e9\u00ed\u00f3\u00fa\u00fc\u00f1"
)

CARACTERES_DIRECCION = CARACTERES_NOMBRE + "0123456789,#/"


def es_nombre_valido(valor=None) -> bool:
    """
    Valida si un nombre de persona o razón social es válido.

    Criterios:
    - Longitud entre 2 y 50 caracteres después de limpiar espacios.
    - Debe contener solo caracteres alfabéticos, espacios y algunos símbolos comunes.

    Args:
        valor (str, optional): El nombre a validar. Defaults to None.

    Returns:
        bool: True si el nombre es válido, False en caso contrario.
    """
    if valor is None:
        return False
    v = colapsar_espacios(limpiar_texto(valor))
    if 2 <= len(v) <= 50:
        return all(ch in CARACTERES_NOMBRE for ch in v)
    return False


def es_cuil_valido(valor=None) -> bool:
    """
    Valida si un CUIL/CUIT es válido.

    Criterios:
    - Debe tener exactamente 11 dígitos.

    Args:
        valor (str, optional): El CUIL a validar. Defaults to None.

    Returns:
        bool: True si el CUIL es válido, False en caso contrario.
    """
    if valor is None:
        return False
    v = solo_digitos(limpiar_texto(valor))
    return len(v) == 11 and v.isdigit()


def es_mail_valido(valor=None) -> bool:
    """
    Valida si un correo electrónico tiene un formato básico.

    Criterios:
    - Longitud entre 5 y 120 caracteres.
    - Debe contener los caracteres '@' y '.'.

    Args:
        valor (str, optional): El mail a validar. Defaults to None.

    Returns:
        bool: True si el mail es válido, False en caso contrario.
    """
    if valor is None:
        return False
    v = limpiar_texto(valor)
    return 5 <= len(v) <= 120 and ("@" in v and "." in v)


def es_telefono_valido(valor=None) -> bool:
    """
    Valida si un número de teléfono es válido.

    Criterios:
    - Debe tener exactamente 11 dígitos (código de área + número).

    Args:
        valor (str, optional): El teléfono a validar. Defaults to None.

    Returns:
        bool: True si el teléfono es válido, False en caso contrario.
    """
    if valor is None:
        return False
    v = solo_digitos(limpiar_texto(valor))
    return len(v) == 11 and v.isdigit()


def es_direccion_valida(valor=None) -> bool:
    """
    Valida si una dirección es válida.

    Criterios:
    - Longitud entre 2 y 120 caracteres.
    - Admite caracteres alfanuméricos y símbolos comunes para direcciones.

    Args:
        valor (str, optional): La dirección a validar. Defaults to None.

    Returns:
        bool: True si la dirección es válida, False en caso contrario.
    """
    if valor is None:
        return False
    v = colapsar_espacios(limpiar_texto(valor))
    if 2 <= len(v) <= 120:
        return all(ch in CARACTERES_DIRECCION for ch in v)
    return False


def es_dni_valido(valor=None) -> bool:
    """
    Valida si un DNI es válido.

    Criterios:
    - Debe tener exactamente 8 dígitos.

    Args:
        valor (str, optional): El DNI a validar. Defaults to None.

    Returns:
        bool: True si el DNI es válido, False en caso contrario.
    """
    if valor is None:
        return False
    v = solo_digitos(limpiar_texto(valor))
    return len(v) == 8 and v.isdigit()
