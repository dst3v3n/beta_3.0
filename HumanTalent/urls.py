"""HumanTalent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from .views import Index , pag_404_not_found
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', Index.admin , name='admin_link'),
    path('', Index.index , name='index'),
    path('registro/', Index.registro ,  name='registro'),
    path('login/', Index.login ,  name='login'),

    path('users/' , include('users.urls')),
    path('company/' , include('company.urls')),
    path('perfil/' , include('perfil_user.urls')),
    path('admins/' , include('admins.urls')),
    path('curriculum/' , include('HojaVida.urls')),
    path('requisicion/' , include('requisicion.urls')),
    path('ponderacion/' , include('Ponderacion.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pag_404_not_found
