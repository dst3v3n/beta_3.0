from django.shortcuts import render
from typing import Any
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from users.models import User_normal
from . models import Perfil
from .forms import Form_Info_Perfil
from admins.forms import Form_Name
from admins.models import Myuser
from HojaVida.models import Personal_information
from HojaVida.forms import Form_Person_Info
from django.contrib.auth.mixins import LoginRequiredMixin
from HojaVida.mixin import EmailVerificadoMixin
from django.views.generic import TemplateView , ListView
from .alerta import alertas

@login_required
def mostrar_perfil(request):
    perfil_user = request.User_normal.Perfil  
    return render(request, 'perfiluser.html', {'perfil_user': perfil_user})


def usuarioFoto(request):
    get_foto = Perfil.objects.all()
    data={
        'get_foto': get_foto
    }
    return render(request, 'perfiluser.html',data)

def usuarioFondo(request):
    get_fondo = Perfil.objects.all()
    data2={
        'get_fondo': get_fondo
    }
    return render(request, 'perfiluser.html',data2)

class ver_perfil (LoginRequiredMixin , EmailVerificadoMixin, TemplateView):

    template_name = 'perfiluser.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        form_requi = Form_Info_Perfil(instance=Perfil.objects.get(id= self.kwargs['id']))
        form_admin = Form_Name (instance= Myuser.objects.get(pk=self.request.COOKIES.get('User_id')))
        form_hoja = Form_Person_Info(instance= Personal_information.objects.get(id_myuser=self.request.COOKIES.get('User_id')))
        data = {
            'form_requi' : form_requi,
            'form_name' : form_admin,
            'form_person_info' : form_hoja,
            }
        context.update (data)
        return context
    
class save_perfil:

    def info_perfil_f (request):
        if request.method == 'POST':
            form = Form_Info_Perfil (request.POST)
            if form.is_valid() :
                info = form.save(commit = False)
                info.id_myuser_id = request.COOKIES.get('User_id')
                info.save ()
                alertas.save (request , 'Informacion de Perfil')
                return redirect ('info_perfil')


    def edit_requi (request , id):
        if request.method == 'POST':
            usuario = Perfil.objects.get (pk = id)
            form = Form_Info_Perfil (request.POST , request.FILES, instance= usuario)
            if form.is_valid ():
                form.save ()
                return redirect ('info_perfi')
 # views.py


    def name_vista(request):
        nombre_usuario = Form_Name (request.POST , instance = Myuser.objects.get(pk = request.COOKIES.get ('User_id')))
    
        return render(request, 'perfiluser.html', {'name': nombre_usuario})