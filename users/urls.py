from django.urls import path , include
from .views import Acceso_User , view_user

urlpatterns = [
    path('registro/usuario/', Acceso_User.registrar , name='registro_user'),
    path('view/perfil/', view_user.perfil , name='view_perfil'),
]
