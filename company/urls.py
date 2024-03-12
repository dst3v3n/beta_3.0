from django.urls import path
from .views import Acceso_Company, vistas

urlpatterns = [
    path('registro/company/', Acceso_Company.registrar , name='registro_company'),
    path('crearrequisicion/company/', vistas.requisicion , name='crearrequisicion_company'),
    path('verrequisicion/company/', vistas.verrequisicionm , name='verrequisicion_company'),
]
