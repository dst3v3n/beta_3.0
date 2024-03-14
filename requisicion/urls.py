from django.urls import path
from .views import save_requi, create_oferta
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/hoja/', create_oferta.as_view() ,  name='create_oferta'),
    path('save/requi/', save_requi.info_requi ,  name='save_info_requi'),
]