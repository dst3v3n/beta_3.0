from django.urls import path , include
from .views import Acceso_User

urlpatterns = [
    path('registro/usuario/', Acceso_User.registrar , name='registro_user'),
]
