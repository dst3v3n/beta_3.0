from django.shortcuts import render , redirect
from admins.admin import UserCreationForm
from .forms import forms_user
from admins.models import Myuser
from django.core.exceptions import ValidationError

# Create your views here.

class Acceso_User:
    def registrar (request):
        if request.method == 'POST':
            email = request.POST ['email']
            password1 = request.POST ['password1']
            password2 = request.POST ['password2']
            form = UserCreationForm(request.POST)
            form1 = forms_user (request.POST)
            if password1 and password2 and password1 != password2:
                raise ValidationError ("La contraseña no coincide")
            else:
                if form.is_valid():
                    if form1.is_valid ():
                        form.save()
                        info = form1.save(commit=False)
                        h = Myuser.objects.filter (email = email).values ('id')
                        for i in h:
                            x =  i['id']
                        info.id_myuser_id = x
                        info.save ()
                        return redirect('index')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

class view_user:

    def perfil (request):
        return render (request , 'perfiluser.html')
