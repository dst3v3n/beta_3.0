from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ver_perfil, save_perfil


urlpatterns = [
    path('perfil/' , views.mostrar_perfil , name='perfil_usuarios '),
    path('perfil/<int:id_myuser>/', ver_perfil.as_view(), name='info_perfil'),
    path('save/', save_perfil.info_perfil_f ,  name='save_info_perfil'),
    path('mostrar/', save_perfil.name_vista ,  name='nombre_usuario')
]
