from django.db import models
from django.utils import timezone


class Especialidad(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class ObraSocial(models.Model):
    # Mejora 1: nueva tabla (entidad adicional)
    nombre = models.CharField(max_length=120, unique=True)
    cobertura = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    # Mejora 2: CHOICES
    class Estado(models.TextChoices):
        ACTIVO = "ACTIVO", "Activo"
        INACTIVO = "INACTIVO", "Inactivo"

    nombre = models.CharField(max_length=255)
    edad = models.PositiveIntegerField()
    direccion = models.CharField(max_length=255)
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.ACTIVO)
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    medicamentos = models.ManyToManyField(Medicamento, blank=True)

    def __str__(self):
        return self.nombre

class ConsultaMedica(models.Model):
    class Estado(models.TextChoices):
        AGENDADA = "AGENDADA", "Agendada"
        REALIZADA = "REALIZADA", "Realizada"
        CANCELADA = "CANCELADA", "Cancelada"

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=10, choices=Estado.choices, default=Estado.AGENDADA)

    def __str__(self):
        return f"{self.paciente} con {self.medico} ({self.fecha})"

class RecetaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, default=None)  # Permitir NULL, asignar valor predeterminado None
    fecha = models.DateField()
    medicamentos = models.ManyToManyField(Medicamento, blank=True)

    def __str__(self):
        return f"Receta {self.paciente} - {self.fecha}"
