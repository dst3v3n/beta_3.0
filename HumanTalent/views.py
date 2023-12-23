from django.shortcuts import render , redirect
from users.forms import forms_user
from company.forms import forms_company
from admins.admin import UserCreationForm
from admins.forms import Form_Acceso
from django.contrib import admin


class Index:
    def index (request):
        if request.COOKIES.get ('type_user') == 'Admin' or request.COOKIES.get ('type_user') == 'Superuser':
            return redirect ('AdminIndex')
        else:
            if request.COOKIES.get('Login_status'):
                botones = False
                barra = True
            else:
                botones = True
                barra = False

            if request.COOKIES.get('type_user') == 'Company':
                acceso_empresa =  True
            else:
                acceso_empresa = False

            data = {
                'boton': botones ,
                'barra' : barra ,
                'empresa' : acceso_empresa,
            }

            return render (request , 'index.html' , data)

    def registro (request):
        if request.COOKIES.get ('Login_status') == 'True':
            return redirect ('index')
        else:
            form_admin = UserCreationForm ()
            form_user = forms_user ()
            form_company = forms_company ()
            data = {
                'Form_Admin' : form_admin,
                'Form_User' : form_user,
                'Form_Company' : form_company,
            }
            return render(request , 'registro.html' , data)

    def login(request):
        if request.COOKIES.get ('Login_status') == 'True':
            return redirect ('index')
        else:
            form = Form_Acceso ()
            data = {'form': form}
            return render(request , 'login.html' , data)

    def admin (request):
        return (request , admin.site.urls)
