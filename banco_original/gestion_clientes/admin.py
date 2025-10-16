from django.contrib import admin
from .models import PersonaFisica, PersonaJuridica


@admin.register(PersonaFisica)
class PersonaFisicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuil', 'dni', 'mail', 'telefono', 'direccion')
    search_fields = ('nombre', 'cuil', 'dni', 'mail')
    list_filter = ('nombre',)
    ordering = ('nombre',)

    def get_readonly_fields(self, request, obj = ...):
        if obj:  # Si el obj ya existe (edición)
            return ('dni', 'cuil')
        return ()


@admin.register(PersonaJuridica)
class PersonaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuil', 'razon_social', 'mail', 'telefono', 'direccion')
    search_fields = ('nombre', 'cuil', 'razon_social', 'mail')
    list_filter = ('nombre',)
    ordering = ('nombre',)

    def get_readonly_fields(self, request, obj = ...):
        if obj:  # Si el obj ya existe (edición)
            return ('cuil',)
        return ()
