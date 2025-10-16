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
    if valor is None:
        return False
    v = colapsar_espacios(limpiar_texto(valor))
    if 2 <= len(v) <= 50:
        return all(ch in CARACTERES_NOMBRE for ch in v)
    return False


def es_cuil_valido(valor=None) -> bool:
    if valor is None:
        return False
    v = solo_digitos(limpiar_texto(valor))
    return len(v) == 11 and v.isdigit()


def es_mail_valido(valor=None) -> bool:
    if valor is None:
        return False
    v = limpiar_texto(valor)
    return 5 <= len(v) <= 120 and ("@" in v and "." in v)


def es_telefono_valido(valor=None) -> bool:
    if valor is None:
        return False
    v = solo_digitos(limpiar_texto(valor))
    return len(v) == 11 and v.isdigit()


def es_direccion_valida(valor=None) -> bool:
    if valor is None:
        return False
    v = colapsar_espacios(limpiar_texto(valor))
    if 2 <= len(v) <= 120:
        return all(ch in CARACTERES_DIRECCION for ch in v)
    return False


def es_dni_valido(valor=None) -> bool:
    if valor is None:
        return False
    v = solo_digitos(limpiar_texto(valor))
    return len(v) == 8 and v.isdigit()
