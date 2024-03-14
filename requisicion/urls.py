from django.urls import path
from .views import save_requi, create_oferta, vista
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/oferta/', create_oferta.as_view() ,  name='create_oferta'),
    path('save/oferta/', save_requi.info_requi ,  name='save_info_requi'),
    path('ver/' , vista.ver , name='verrequisicion'),
]




