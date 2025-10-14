from django.contrib import admin
from django.urls import path, include  # Necesitamos 'include' para las rutas de la app 'api'

# Importar las vistas de 'drf-spectacular'
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),  # Rutas para el admin de Django

    # Rutas para la documentación de la API con Swagger
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Ruta para el esquema OpenAPI

    # Incluir las rutas de la aplicación 'api'
    path('api/', include('api.urls')),  # Incluimos las rutas de la API
]
