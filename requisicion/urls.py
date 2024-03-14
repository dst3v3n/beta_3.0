from django.urls import path
from .views import vista
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('ver/' , vista.ver , name='verrequisicion'),
    path('crear/' , vista.crear , name='crearrequisicion'),
]
