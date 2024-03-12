from django.shortcuts import render , redirect
from admins.admin import UserCreationForm
from .forms import forms_company
from admins.models import Myuser
from django.core.exceptions import ValidationError

# Create your views here.

class Acceso_Company:
    def registrar (request):
        if request.method == 'POST':
            email = request.POST ['email']
            password1 = request.POST ['password1']
            password2 = request.POST ['password2']
            if password1 and password2 and password1 != password2:
                raise ValidationError ("La contraseña no coincide")
            else:
                form = UserCreationForm(request.POST)
                form1 = forms_company (request.POST)
                if form.is_valid():
                    if form1.is_valid ():
                        info1 = form.save(commit=False)
                        info = form1.save(commit=False)
                        info1.type_user = 'Company'
                        info1.save ()
                        h = Myuser.objects.filter (email = email).values ('id')
                        for i in h:
                            x =  i['id']
                        info.id_myuser_id  = x
                        info.save ()
                        return redirect('index')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

class vistas :
    def requisicion (request):
        return render (request,'crearrequisicion.html')
    def verrequisicionm (request):
        return render (request,'verrequisicion.html')