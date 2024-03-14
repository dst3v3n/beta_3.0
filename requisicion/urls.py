from django.urls import path
from .views import save_requi, create_oferta , vista

urlpatterns = [
    path('create/oferta/', create_oferta.as_view() ,  name='create_oferta'),
    path('save/oferta/', save_requi.info_requi ,  name='save_info_requi'),
    path('mirar ofertas/' , vista.ver , name='veroferta'),
]
