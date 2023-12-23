from django.urls import path , include
from .views import acceso , Edicion

urlpatterns = [
    path('acceso/' , acceso.login , name='acceso'),
    path('logout/ ', acceso.logout ,  name='logout'),
    path('admins/index/' , acceso.index_admin ,  name='AdminIndex'),
    path('visualizar_users/' , Edicion.visualizar_users , name='view'),
    path('registro/user/' , Edicion.Form_User , name='registro_user1'),
    path('registro/company/' , Edicion.Form_Company , name='registro_company1'),
    path('registro/admin/' , Edicion.Form_Admin , name='registro_admin1'),
    path('registro/administradores/', acceso.registrar , name='registro_admin'),

    path('editar_user/<int:id_usuario>' , Edicion.edit_users , name='edit_user'),
    path('actualizar/user/<int:id_usuario>' , Edicion.updateUser , name="update_user"),
    path('actualizar/company/<int:id_usuario>' , Edicion.updateCompany , name="update_company"),
    path("eliminar_usuario/<int:id_usuario>" , Edicion.deleteUsuario , name="delete_user"),
]
