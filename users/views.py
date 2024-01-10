from django.shortcuts import render , redirect
from admins.admin import UserCreationForm
from .forms import forms_user
from admins.models import Myuser
from admins.admin import UserCreationForm
import sweetify

# Create your views here.

class Acceso_User:
    def registrar (request):
        if request.method == 'POST':
            email = request.POST ['email']
            password1 = request.POST ['password1']
            password2 = request.POST ['password2']
            form = UserCreationForm(request.POST)
            form1 = forms_user (request.POST)
            if password1 and password2 and password1 == password2:
                if form.is_valid():
                    if form1.is_valid ():
                        form.save()
                        info = form1.save(commit=False)
                        h = Myuser.objects.filter (email = email).values ('id')
                        for i in h:
                            x =  i['id']
                        info.id_myuser_id = x
                        info.save ()
                        sweetify.success (request, 'Cuenta creada', text='Tu cuenta ha sido creada', persistent='ok')
                        return redirect ("registro")
            else:
                sweetify.error (request , "Las contraseñas no son iguales" ,  persistent='Ok')
                return redirect ("registro")

        sweetify.warning (request , "El correo ya existe" , persistent='Ok')
        return redirect ("registro")

class view_user:

    def perfil (request):
        return render (request , 'perfiluser.html')
