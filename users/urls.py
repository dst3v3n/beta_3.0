from django.urls import path , include
from .views import Acceso_User , view_user , visualizar_ofertas, ver_requi2

urlpatterns = [
    path('registro/usuario/', Acceso_User.registrar , name='registro_user'),
    path('view/perfil/', view_user.perfil , name='view_perfil'),
    path('visualizar/ofertas/', visualizar_ofertas.as_view() ,  name='visualizar_ofertas'),
    path('visualizar/requi/<int:id_myuser>/', ver_requi2.as_view() ,  name='ver_ofertas'),
]
