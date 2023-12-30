from django.urls import path , include
from .views import visualizar , Edicion_hj
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('view/hoja/', visualizar.view_hoja ,  name='view_hoja'),
    path('save/personal_information/', Edicion_hj.save_info ,  name='save_info_hoja'),
    path('save/education/', Edicion_hj.save_education ,  name='save_education_hoja'),
    path('save/experience/', Edicion_hj.save_experience ,  name='save_experience_hoja'),
    path('save/reference/', Edicion_hj.save_reference ,  name='save_reference_hoja'),
    path('save/aditional/', Edicion_hj.save_aditional ,  name='save_aditional_hoja'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
