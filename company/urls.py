from django.urls import path
from .views import Acceso_Company, vistas

urlpatterns = [
    path('registro/company/', Acceso_Company.registrar , name='registro_company'),
    path('requisicion/company/', vistas.requisicion , name='crearrequisicion_company'),
]
