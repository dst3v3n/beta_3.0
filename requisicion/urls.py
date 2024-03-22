from django.urls import path
from .views import save_requi, create_oferta  , consultar_ofer , ver_requi , save_form , delete_requi

urlpatterns = [
    path('create/oferta/', create_oferta.as_view() ,  name='create_oferta'),
    path('save/oferta/', save_form.as_view() ,  name='save_info_requi'),
    path('consultar/ofertas/<int:id_myuser>/', consultar_ofer.as_view(), name='consultar_ofer'),
    path('consultar/requisicion/<int:id_myuser>/<int:id_oferta>/', ver_requi.as_view(), name='ver_oferta'),
    path('ver/oferta/<int:id>/', save_requi.edit_requi ,  name='edit_info_requi'),
    path('delete/oferta/<int:id_requisicion>/', delete_requi.as_view(),  name='delete_info_requi'),
]
