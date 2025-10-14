from django.urls import path
from . import views  # Importamos las vistas que tenemos en views.py


urlpatterns = [
    path('especialidades/', views.EspecialidadListCreate.as_view(), name='especialidad-list-create'),
    path('especialidades/<int:pk>/', views.EspecialidadRetrieveUpdateDestroy.as_view(), name='especialidad-detail'),
    path('pacientes/', views.PacienteListCreate.as_view(), name='paciente-list-create'),
    path('pacientes/<int:pk>/', views.PacienteRetrieveUpdateDestroy.as_view(), name='paciente-detail'),
    path('medicos/', views.MedicoListCreate.as_view(), name='medico-list-create'),
    path('medicos/<int:pk>/', views.MedicoRetrieveUpdateDestroy.as_view(), name='medico-detail'),
    path('consultas/', views.ConsultaMedicaListCreate.as_view(), name='consulta-list-create'),
    path('consultas/<int:pk>/', views.ConsultaMedicaRetrieveUpdateDestroy.as_view(), name='consulta-detail'),
    path('tratamientos/', views.TratamientoListCreate.as_view(), name='tratamiento-list-create'),
    path('tratamientos/<int:pk>/', views.TratamientoRetrieveUpdateDestroy.as_view(), name='tratamiento-detail'),
    path('medicamentos/', views.MedicamentoListCreate.as_view(), name='medicamento-list-create'),
    path('medicamentos/<int:pk>/', views.MedicamentoRetrieveUpdateDestroy.as_view(), name='medicamento-detail'),
    path('recetas/', views.RecetaMedicaListCreate.as_view(), name='receta-list-create'),
    path('recetas/<int:pk>/', views.RecetaMedicaRetrieveUpdateDestroy.as_view(), name='receta-detail'),
]
