from django.urls import path
from .views import save_requi, create_oferta , vista , consultar_ofer

urlpatterns = [
    path('create/oferta/', create_oferta.as_view() ,  name='create_oferta'),
    path('save/oferta/', save_requi.info_requi ,  name='save_info_requi'),
    path('company/<int:id_myuser>/', consultar_ofer.as_view(), name='consultar_ofer'),
]
