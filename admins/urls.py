from django.urls import path , include
from .views import acceso , Edicion , Verification

urlpatterns = [
    path('acceso/' , acceso.login , name='acceso'),
    path('acceso/bloqueado/' , acceso.lockout , name='lockout'),
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

    path('verify-email/', Verification.verify_email, name='verify-email'),
    path('verify-email/done/', Verification.verify_email_done, name='verify-email-done'),
    path('verify-email-confirm/<uidb64>/<token>/', Verification.verify_email_confirm, name='verify-email-confirm'),
    path('verify-email/complete/', Verification.verify_email_complete, name='verify-email-complete'),
]
