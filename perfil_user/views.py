from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from users.models import User_normal
from . models import Perfil
from admins.models import Myuser
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