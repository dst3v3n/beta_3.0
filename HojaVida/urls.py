from django.urls import path
from .views import save_hj , create_hoja ,Visualizar_hoja
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/hoja/', create_hoja.as_view() ,  name='create_hoja'),
    path('view/hoja/', Visualizar_hoja.as_view() ,  name='view_hoja'),

    path('save/personal_information/', save_hj.save_info ,  name='save_info_hoja'),
    path('save/education/', save_hj.save_education ,  name='save_education_hoja'),
    path('save/experience/', save_hj.save_experience ,  name='save_experience_hoja'),
    path('save/reference/', save_hj.save_reference ,  name='save_reference_hoja'),
    path('save/aditional/', save_hj.save_aditional ,  name='save_aditional_hoja'),

    path('edit/personal_information/', save_hj.edit_information ,  name='edit_info_hoja'),
    path('edit/education/<int:id_usuario>/' , save_hj.edit_education , name='edit_education_hoja'),
    path('edit/experience/<int:id_usuario>/' , save_hj.edit_experience , name='edit_experince_hoja'),
    path('edit/persona_reference/<int:id_usuario>/' , save_hj.edit_personal_reference , name='edit_personal_reference_hoja'),
    path('edit/business_reference/<int:id_usuario>/' , save_hj.edit_bussiness_reference , name='edit_business_reference_hoja'),
    path('edit/aditional/', save_hj.edit_aditional ,  name='edit_aditional_hoja'),

    path('delete/personal_information/', save_hj.delete_information ,  name='delete_info_hoja'),
    path('delete/education/<int:id_usuario>/', save_hj.delete_education ,  name='delete_education_hoja'),
    path('delete/experience/<int:id_usuario>/', save_hj.delete_experience ,  name='delete_experience_hoja'),
    path('delete/persona_reference/<int:id_usuario>/' , save_hj.delete_personal_reference , name='delete_personal_reference_hoja'),
    path('delete/business_reference/<int:id_usuario>/' , save_hj.delete_bussiness_reference , name='delete_business_reference_hoja'),
    path('delete/aditional/', save_hj.delete_aditional ,  name='delete_aditional_hoja'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
