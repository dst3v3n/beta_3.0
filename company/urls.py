from django.urls import path
from .views import Acceso_Company

urlpatterns = [
    path('registro/company/', Acceso_Company.registrar , name='registro_company'),
]
