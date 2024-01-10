from django.shortcuts import render , redirect
from admins.admin import UserCreationForm
from .forms import forms_user
from admins.models import Myuser
from django.contrib import messages
from company.forms import forms_company
from admins.admin import UserCreationForm
from admins.forms import Form_Acceso

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
                        return redirect('index')
            else:
                messages.success (request , "Las contraseñas no son iguales")
                return redirect ("registro")
        else:
            return render ('registro')

class view_user:

    def perfil (request):
        return render (request , 'perfiluser.html')
