from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ver_perfil, save_perfil
# soy


urlpatterns = [

    path('perfil/', ver_perfil.as_view(), name='info_perfil'),
    path('save/', save_perfil.info_perfil_f ,  name='save_info_perfil'),
    path('mostrar/', save_perfil.name_vista ,  name='nombre_usuario')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)