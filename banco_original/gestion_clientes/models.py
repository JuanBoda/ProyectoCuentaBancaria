from django.core.exceptions import ValidationError
from . import validator as v
from django.db import models


class ClienteBase(models.Model):
    nombre = models.CharField(max_length=50)
    cuil = models.CharField(max_length=11, unique=True)
    mail = models.EmailField(max_length=120, unique=True)
    direccion = models.CharField(max_length=120)
    telefono = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]
        abstract = True

    def clean(self):
        if not v.es_nombre_valido(self.nombre):
            raise ValidationError({"nombre": "El nombre no es válido."})
        if not v.es_cuil_valido(self.cuil):
            raise ValidationError({"cuil": "El CUIL no es válido."})
        if not v.es_mail_valido(self.mail):
            raise ValidationError({"mail": "El mail no es válido."})
        if not v.es_direccion_valida(self.direccion):
            raise ValidationError({"direccion": "La dirección no es válida."})
        if not v.es_telefono_valido(self.telefono):
            raise ValidationError({"telefono": "El teléfono no es válido."})

        # CUIL inmutable
        if self.pk is not None:
            cliente_original = type(self).objects.get(pk=self.pk)
            if cliente_original.cuil != self.cuil:
                raise ValidationError({"cuil": "El CUIL no puede ser modificado."})

    def __str__(self):
        return f"{self.nombre} - CUIL/CUIT:{self.cuil}"


class PersonaFisica(ClienteBase):
    dni = models.CharField(max_length=8, unique=True)

    class Meta:
        verbose_name = "Persona Física"
        verbose_name_plural = "Personas Físicas"

    def clean(self):
        # Ejecutar validaciones de la clase base
        super().clean()

        if self.dni and not v.es_dni_valido(self.dni):
            raise ValidationError(
                {"dni": "El DNI debe tener exactamente 8 dígitos numéricos."}
            )

        # DNI inmutable
        if self.pk is not None:
            cliente_original = type(self).objects.get(pk=self.pk)
            if cliente_original.dni != self.dni:
                raise ValidationError({"dni": "El DNI no puede ser modificado."})


class PersonaJuridica(ClienteBase):
    razon_social = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Persona Jurídica"
        verbose_name_plural = "Personas Jurídicas"

    def clean(self):
        # Ejecutar validaciones de la clase base
        super().clean()

        # Comprobación adicional explícita (la validación de CUIL ya se realiza en ClienteBase)
        if len(self.cuil) != 11 or not self.cuil.isdigit():
            raise ValidationError(
                {"cuil": "El CUIL/CUIT debe tener exactamente 11 dígitos numéricos."}
            )
