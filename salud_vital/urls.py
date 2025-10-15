from django.contrib import admin
from django.urls import path, include  # Necesitamos 'include' para incluir las rutas de 'api'
from django.views.generic import TemplateView

# Importar vistas de la documentación de la API
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),  # Rutas para el panel de administración de Django

    # Ruta principal que carga base.html directamente
    path('', TemplateView.as_view(template_name='base.html'), name='home'),  # Carga base.html cuando accedas a "/"


    # Rutas para la documentación de la API con Swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Incluir las rutas de la app 'api'
    path('api/', include('api.urls')),  # Asegúrate de que la app 'api' esté incluida
]

