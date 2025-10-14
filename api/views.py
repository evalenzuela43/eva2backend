from rest_framework import generics
from .models import Especialidad, Paciente, Medico, ConsultaMedica, Tratamiento, Medicamento, RecetaMedica
from .serializers import EspecialidadSerializer, PacienteSerializer, MedicoSerializer, ConsultaMedicaSerializer, TratamientoSerializer, MedicamentoSerializer, RecetaMedicaSerializer

class EspecialidadListCreate(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class EspecialidadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class PacienteListCreate(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoListCreate(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class ConsultaMedicaListCreate(generics.ListCreateAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class ConsultaMedicaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class TratamientoListCreate(generics.ListCreateAPIView):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class TratamientoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentoListCreate(generics.ListCreateAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class MedicamentoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class RecetaMedicaListCreate(generics.ListCreateAPIView):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer

class RecetaMedicaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer
