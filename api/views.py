from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import generics, permissions, filters
from .models import (
    Especialidad, Medico, Medicamento,
    Paciente, RecetaMedica, Tratamiento, ConsultaMedica, ObraSocial
)
from .serializers import (
    EspecialidadSerializer, PacienteSerializer, MedicoSerializer,
    ConsultaMedicaSerializer, TratamientoSerializer, MedicamentoSerializer,
    RecetaMedicaSerializer, ObraSocialSerializer
)
from .forms import (
    EspecialidadForm, MedicoForm, MedicamentoForm,
    PacienteForm, RecetaMedicaForm, TratamientoForm, ConsultaMedicaForm
)

#------------view de home-----------

# Vista de inicio
class HomeView(TemplateView):
    template_name = 'base.html'  # Asegúrate de que 'base.html' esté en la carpeta 'templates'

# ---------- API (DRF) ----------

class EspecialidadListCreate(generics.ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nombre", "descripcion"]
    ordering_fields = ["nombre"]

class EspecialidadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class PacienteListCreate(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filterset_fields = ["estado", "obra_social"]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nombre", "direccion"]
    ordering_fields = ["nombre", "edad"]

class PacienteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoListCreate(generics.ListCreateAPIView):
    queryset = Medico.objects.select_related("especialidad").all()
    serializer_class = MedicoSerializer
    filterset_fields = {"especialidad": ["exact"]}
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nombre", "especialidad__nombre"]
    ordering_fields = ["nombre"]

class MedicoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class ConsultaMedicaListCreate(generics.ListCreateAPIView):
    queryset = ConsultaMedica.objects.select_related("paciente", "medico").all()
    serializer_class = ConsultaMedicaSerializer
    filterset_fields = {"paciente": ["exact"], "medico": ["exact"], "estado": ["exact"]}
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["descripcion", "paciente__nombre", "medico__nombre"]
    ordering_fields = ["fecha"]

class ConsultaMedicaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsultaMedica.objects.all()
    serializer_class = ConsultaMedicaSerializer

class TratamientoListCreate(generics.ListCreateAPIView):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["nombre", "descripcion"]

class TratamientoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer

class MedicamentoListCreate(generics.ListCreateAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["nombre", "descripcion"]

class MedicamentoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class RecetaMedicaListCreate(generics.ListCreateAPIView):
    queryset = RecetaMedica.objects.select_related("paciente", "medico").all()
    serializer_class = RecetaMedicaSerializer
    filterset_fields = {"paciente": ["exact"], "medico": ["exact"]}

class RecetaMedicaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecetaMedica.objects.all()
    serializer_class = RecetaMedicaSerializer

class ObraSocialListCreate(generics.ListCreateAPIView):
    queryset = ObraSocial.objects.all()
    serializer_class = ObraSocialSerializer

class ObraSocialRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ObraSocial.objects.all()
    serializer_class = ObraSocialSerializer

# ---------- HTML (CBV + templates que tú ya tienes) ----------

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser
#----------------------------------------------
# Paciente (accesible para usuarios)
#---------------------------------------------
class PacienteListView(ListView):
    model = Paciente
    template_name = "paciente_list.html"
    context_object_name = "pacientes"

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "paciente_form.html"
    success_url = reverse_lazy("paciente-list-ui")

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "paciente_form.html"
    success_url = reverse_lazy("paciente-list-ui")

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = "paciente_confirm_delete.html"
    success_url = reverse_lazy("paciente-list-ui")
#
# Medico (solo admin)
#
class MedicoListView(AdminRequiredMixin, ListView):
    model = Medico
    template_name = "medico_list.html"
    context_object_name = "medicos"

class MedicoCreateView(AdminRequiredMixin, CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medico_form.html"
    success_url = reverse_lazy("medico-list-ui")

class MedicoUpdateView(AdminRequiredMixin, UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medico_form.html"
    success_url = reverse_lazy("medico-list-ui")

class MedicoDeleteView(AdminRequiredMixin, DeleteView):
    model = Medico
    template_name = "medico_confirm_delete.html"
    success_url = reverse_lazy("medico-list-ui")

# Especialidad (solo admin)
class EspecialidadListView(AdminRequiredMixin, ListView):
    model = Especialidad
    template_name = "especialidad_list.html"
    context_object_name = "especialidades"

class EspecialidadCreateView(AdminRequiredMixin, CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = "especialidad_form.html"
    success_url = reverse_lazy("especialidad-list-ui")

class EspecialidadUpdateView(AdminRequiredMixin, UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = "especialidad_form.html"
    success_url = reverse_lazy("especialidad-list-ui")

class EspecialidadDeleteView(AdminRequiredMixin, DeleteView):
    model = Especialidad
    template_name = "especialidad_confirm_delete.html"
    success_url = reverse_lazy("especialidad-list-ui")

# Medicamento (solo admin)
class MedicamentoListView(AdminRequiredMixin, ListView):
    model = Medicamento
    template_name = "medicamento_list.html"
    context_object_name = "medicamentos"

class MedicamentoCreateView(AdminRequiredMixin, CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = "medicamento_form.html"
    success_url = reverse_lazy("medicamento-list-ui")

class MedicamentoUpdateView(AdminRequiredMixin, UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = "medicamento_form.html"
    success_url = reverse_lazy("medicamento-list-ui")

class MedicamentoDeleteView(AdminRequiredMixin, DeleteView):
    model = Medicamento
    template_name = "medicamento_confirm_delete.html"
    success_url = reverse_lazy("medicamento-list-ui")

# Tratamiento (solo admin)
class TratamientoListView(AdminRequiredMixin, ListView):
    model = Tratamiento
    template_name = "tratamiento_list.html"
    context_object_name = "tratamientos"

class TratamientoCreateView(AdminRequiredMixin, CreateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = "tratamiento_form.html"
    success_url = reverse_lazy("tratamiento-list-ui")

class TratamientoUpdateView(AdminRequiredMixin, UpdateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = "tratamiento_form.html"
    success_url = reverse_lazy("tratamiento-list-ui")

class TratamientoDeleteView(AdminRequiredMixin, DeleteView):
    model = Tratamiento
    template_name = "tratamiento_confirm_delete.html"
    success_url = reverse_lazy("tratamiento-list-ui")

# Receta (solo admin)
class RecetaListView(AdminRequiredMixin, ListView):
    model = RecetaMedica
    template_name = "receta_list.html"
    context_object_name = "recetas"

class RecetaCreateView(AdminRequiredMixin, CreateView):
    model = RecetaMedica
    form_class = RecetaMedicaForm
    template_name = "receta_form.html"
    success_url = reverse_lazy("receta-list-ui")

class RecetaUpdateView(AdminRequiredMixin, UpdateView):
    model = RecetaMedica
    form_class = RecetaMedicaForm
    template_name = "receta_form.html"
    success_url = reverse_lazy("receta-list-ui")

class RecetaDeleteView(AdminRequiredMixin, DeleteView):
    model = RecetaMedica
    template_name = "receta_confirm_delete.html"
    success_url = reverse_lazy("receta-list-ui")

# Consulta (agendable por usuarios)
class ConsultaListView(ListView):
    model = ConsultaMedica
    template_name = "consulta_list.html"
    context_object_name = "consultas"

class ConsultaCreateView(CreateView):
    model = ConsultaMedica
    form_class = ConsultaMedicaForm
    template_name = "consulta_form.html"
    success_url = reverse_lazy("consulta-list-ui")

class ConsultaUpdateView(UpdateView):
    model = ConsultaMedica
    form_class = ConsultaMedicaForm
    template_name = "consulta_form.html"
    success_url = reverse_lazy("consulta-list-ui")

class ConsultaDeleteView(DeleteView):
    model = ConsultaMedica
    template_name = "consulta_confirm_delete.html"
    success_url = reverse_lazy("consulta-list-ui")
