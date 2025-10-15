from django.urls import path
from . import views

urlpatterns = [
    # ---------- API (JSON) ----------
    path("especialidades/", views.EspecialidadListCreate.as_view(), name="especialidad-list-create"),
    path("especialidades/<int:pk>/", views.EspecialidadRetrieveUpdateDestroy.as_view(), name="especialidad-detail"),

    path("pacientes/", views.PacienteListCreate.as_view(), name="paciente-list-create"),
    path("pacientes/<int:pk>/", views.PacienteRetrieveUpdateDestroy.as_view(), name="paciente-detail"),

    path("medicos/", views.MedicoListCreate.as_view(), name="medico-list-create"),
    path("medicos/<int:pk>/", views.MedicoRetrieveUpdateDestroy.as_view(), name="medico-detail"),

    path("consultas/", views.ConsultaMedicaListCreate.as_view(), name="consulta-list-create"),
    path("consultas/<int:pk>/", views.ConsultaMedicaRetrieveUpdateDestroy.as_view(), name="consulta-detail"),

    path("tratamientos/", views.TratamientoListCreate.as_view(), name="tratamiento-list-create"),
    path("tratamientos/<int:pk>/", views.TratamientoRetrieveUpdateDestroy.as_view(), name="tratamiento-detail"),

    path("medicamentos/", views.MedicamentoListCreate.as_view(), name="medicamento-list-create"),
    path("medicamentos/<int:pk>/", views.MedicamentoRetrieveUpdateDestroy.as_view(), name="medicamento-detail"),

    path("recetas/", views.RecetaMedicaListCreate.as_view(), name="receta-list-create"),
    path("recetas/<int:pk>/", views.RecetaMedicaRetrieveUpdateDestroy.as_view(), name="receta-detail"),

    path("obrasocial/", views.ObraSocialListCreate.as_view(), name="obrasocial-list-create"),
    path("obrasocial/<int:pk>/", views.ObraSocialRetrieveUpdateDestroy.as_view(), name="obrasocial-detail"),

    # ---------- HTML (Templates que ya tienes) ----------
    # Paciente
    path("ui/pacientes/", views.PacienteListView.as_view(), name="paciente-list-ui"),
    path("ui/pacientes/nuevo/", views.PacienteCreateView.as_view(), name="paciente-create-ui"),
    path("ui/pacientes/editar/<int:pk>/", views.PacienteUpdateView.as_view(), name="paciente-edit-ui"),  # Esto es para editar un paciente
    path("ui/pacientes/eliminar/<int:pk>/", views.PacienteDeleteView.as_view(), name="paciente-delete-ui"),
    
    # Medico (solo admin)
    
    path("ui/medicos/", views.MedicoListView.as_view(), name="medico-list-ui"),
    path("ui/medicos/nuevo/", views.MedicoCreateView.as_view(), name="medico-create-ui"),
    path("ui/medicos/editar/<int:pk>/", views.MedicoUpdateView.as_view(), name="medico-edit-ui"),
    path("ui/medicos/eliminar/<int:pk>/", views.MedicoDeleteView.as_view(), name="medico-delete-ui"),

    # Especialidad (solo admin)
    
    path("ui/especialidades/", views.EspecialidadListView.as_view(), name="especialidad-list-ui"),
    path("ui/especialidades/nuevo/", views.EspecialidadCreateView.as_view(), name="especialidad-create-ui"),
    path("ui/especialidades/editar/<int:pk>/", views.EspecialidadUpdateView.as_view(), name="especialidad-edit-ui"),
    path("ui/especialidades/eliminar/<int:pk>/", views.EspecialidadDeleteView.as_view(), name="especialidad-delete-ui"),

    # Medicamento (solo admin)
    
    path("ui/medicamentos/", views.MedicamentoListView.as_view(), name="medicamento-list-ui"),
    path("ui/medicamentos/nuevo/", views.MedicamentoCreateView.as_view(), name="medicamento-create-ui"),
    path("ui/medicamentos/editar/<int:pk>/", views.MedicamentoUpdateView.as_view(), name="medicamento-edit-ui"),
    path("ui/medicamentos/eliminar/<int:pk>/", views.MedicamentoDeleteView.as_view(), name="medicamento-delete-ui"),

    # Tratamiento (solo admin)
    path("ui/tratamientos/", views.TratamientoListView.as_view(), name="tratamiento-list-ui"),
    path("ui/tratamientos/nuevo/", views.TratamientoCreateView.as_view(), name="tratamiento-create-ui"),
    path("ui/tratamientos/editar/<int:pk>/", views.TratamientoUpdateView.as_view(), name="tratamiento-edit-ui"),
    path("ui/tratamientos/eliminar/<int:pk>/", views.TratamientoDeleteView.as_view(), name="tratamiento-delete-ui"),

    # Receta (solo admin)
    path("ui/recetas/", views.RecetaListView.as_view(), name="receta-list-ui"),
    path("ui/recetas/nuevo/", views.RecetaCreateView.as_view(), name="receta-create-ui"),
    path("ui/recetas/editar/<int:pk>/", views.RecetaUpdateView.as_view(), name="receta-edit-ui"),
    path("ui/recetas/eliminar/<int:pk>/", views.RecetaDeleteView.as_view(), name="receta-delete-ui"),

    # Consulta (agendable)
    path("ui/consultas/", views.ConsultaListView.as_view(), name="consulta-list-ui"),
    path("ui/consultas/nuevo/", views.ConsultaCreateView.as_view(), name="consulta-create-ui"),
    path("ui/consultas/editar/<int:pk>/", views.ConsultaUpdateView.as_view(), name="consulta-edit-ui"),
    path("ui/consultas/eliminar/<int:pk>/", views.ConsultaDeleteView.as_view(), name="consulta-delete-ui"),
]
