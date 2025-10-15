from rest_framework import serializers
from .models import (
    Especialidad, Medico, Medicamento,
    Paciente, RecetaMedica, Tratamiento, ConsultaMedica, ObraSocial
)

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = "__all__"

class ObraSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObraSocial
        fields = "__all__"

class MedicoSerializer(serializers.ModelSerializer):
    especialidad = EspecialidadSerializer(read_only=True)
    especialidad_id = serializers.PrimaryKeyRelatedField(
        source="especialidad", queryset=Especialidad.objects.all(), write_only=True
    )
    class Meta:
        model = Medico
        fields = ["id", "nombre", "especialidad", "especialidad_id"]

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = "__all__"

class PacienteSerializer(serializers.ModelSerializer):
    obra_social = ObraSocialSerializer(read_only=True)
    obra_social_id = serializers.PrimaryKeyRelatedField(
        source="obra_social", queryset=ObraSocial.objects.all(), write_only=True, allow_null=True, required=False
    )
    class Meta:
        model = Paciente
        fields = ["id", "nombre", "edad", "direccion", "estado", "obra_social", "obra_social_id"]

class TratamientoSerializer(serializers.ModelSerializer):
    medicamentos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Medicamento.objects.all(), required=False
    )
    class Meta:
        model = Tratamiento
        fields = "__all__"

class ConsultaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultaMedica
        fields = "__all__"

class RecetaMedicaSerializer(serializers.ModelSerializer):
    medicamentos = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Medicamento.objects.all(), required=False
    )
    class Meta:
        model = RecetaMedica
        fields = "__all__"
