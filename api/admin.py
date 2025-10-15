from django.contrib import admin
from .models import (
    Especialidad, Medico, Medicamento,
    Paciente, RecetaMedica, Tratamiento, ConsultaMedica, ObraSocial
)

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especialidad")
    search_fields = ("nombre",)
    list_filter = ("especialidad",)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edad", "estado", "obra_social")
    list_filter = ("estado", "obra_social")
    search_fields = ("nombre", "direccion")

@admin.register(Tratamiento)
class TratamientoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    filter_horizontal = ("medicamentos",)

@admin.register(ConsultaMedica)
class ConsultaMedicaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "medico", "fecha", "estado")
    list_filter = ("estado", "fecha", "medico", "paciente")
    search_fields = ("paciente__nombre", "medico__nombre", "descripcion")

@admin.register(RecetaMedica)
class RecetaMedicaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "medico", "fecha")
    list_filter = ("fecha", "medico", "paciente")
    search_fields = ("paciente__nombre", "medico__nombre")
    filter_horizontal = ("medicamentos",)

@admin.register(ObraSocial)
class ObraSocialAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cobertura")
    search_fields = ("nombre",)
