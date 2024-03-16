from django.urls import path
from .views import save_requi, create_oferta  , consultar_ofer , ver_requi

urlpatterns = [
    path('create/oferta/', create_oferta.as_view() ,  name='create_oferta'),
    path('save/oferta/', save_requi.info_requi ,  name='save_info_requi'),
    path('consultar/ofertas/<int:id_myuser>/', consultar_ofer.as_view(), name='consultar_ofer'),
    path('consultar/requisicion/<int:id_myuser>/', ver_requi.as_view(), name='ver_oferta'),
    path('ver/oferta/', save_requi.edit_requi ,  name='edit_info_requi'),
    path('delete/oferta/', save_requi.delete_requi ,  name='delete_info_requi'),
]
