from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Paciente

class PacienteApiTests(APITestCase):
    def test_listar_pacientes(self):
        Paciente.objects.create(nombre="Test A", edad=20, direccion="x", estado=Paciente.Estado.ACTIVO)
        url = reverse("paciente-list-create")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.json()) >= 1)

    def test_crear_paciente(self):
        url = reverse("paciente-list-create")
        payload = {"nombre": "Nuevo", "edad": 30, "direccion": "Calle", "estado": "ACTIVO"}
        res = self.client.post(url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Paciente.objects.filter(nombre="Nuevo").exists())
