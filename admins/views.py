from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from admins.models import Myuser
from users.models import User_normal
from users.forms import forms_user
from company.models import Company
from company.forms import forms_company
from django.contrib.auth.decorators import login_required
from .admin import UserCreationForm
from django.core.exceptions import ValidationError
# Create your views here.

class acceso :
    @login_required
    def index_admin (request):
        return render (request , 'admin_index.html')

    def login (request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                for i in Myuser.objects.filter (email=email).values_list('id' , 'type_user'):
                    id_user = i[0]
                    type_user = i[1]
                response = redirect ('index')
                response.set_cookie ('User_id' , id_user , secure=True , httponly=True , samesite='None')
                response.set_cookie ('Email' , email , secure=True , httponly=True , samesite='None')
                response.set_cookie ('type_user' , type_user , secure=True , httponly=True , samesite='None')
                response.set_cookie ('Login_status' , True , secure=True , httponly=True , samesite='None')
                return response
            else:
                return redirect('login')

    @login_required(redirect_field_name="index")
    def logout (request):
        logout (request)
        response = redirect("index")
        response.delete_cookie('User_id')
        response.delete_cookie('type_user')
        response.delete_cookie('Email')
        response.delete_cookie('Login_status')
        return response

    @login_required(redirect_field_name="index")
    def registrar (request):
        if request.method == 'POST':
            password1 = request.POST ['password1']
            password2 = request.POST ['password2']
            form = UserCreationForm(request.POST)
            if password1 and password2 and password1 != password2:
                raise ValidationError ("La contraseña no coincide")
            else:
                if form.is_valid():
                    info1 = form.save(commit=False)
                    info1.type_user = 'Admin'
                    info1.save ()
                    return redirect('index')
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

class Edicion :
    def Form_User (request):
        form = UserCreationForm ()
        form1 = forms_user ()
        data = {
            'form_admin' : form ,
            'form' : form1 ,
            'user' : True
        }
        return render (request , 'registro_admin.html' , data)

    def Form_Company (request):
        form = UserCreationForm ()
        form1 = forms_company ()
        data = {
            'form_admin' : form ,
            'form' : form1,
            'user' : False
        }
        return render (request , 'registro_admin.html' , data)

    def Form_Admin (request):
        form = UserCreationForm ()
        form1 = forms_user ()
        data = {
            'form_admin' : form ,
            'form' : form1 ,
            'admin' : True ,
            'user' : True ,
        }
        return render (request , 'registro_admin.html' , data)

    def visualizar_users (request):
        get_usuarios = Myuser.objects.all()
        data = {
            'get_usuarios' : get_usuarios ,
        }
        return render (request , 'tabla_users.html' , data)

    def edit_users (request , id_usuario):
        usuario = Myuser.objects.filter(id=id_usuario).first()
        form = UserCreationForm (instance = usuario)
        usuario1 = User_normal.objects.filter (id_myuser = id_usuario).first()
        form1 = forms_user (instance = usuario1)
        usuario2= Company.objects.filter (id_myuser = id_usuario).first()
        form2 = forms_company (instance = usuario2)
        data = {
            "form":form,
            "usuario":usuario,
            "form1":form1,
            "usuario1":usuario1,
            "form2":form2,
            "usuario2":usuario2,
        }
        return render(request , "usuarioEdit.html" , data)

    def updateUser(request , id_usuario):
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 and password2 and password1 != password2:
            raise ValidationError ("La contraseña no coincide")
        usuario = Myuser.objects.get(pk=id_usuario)
        form = UserCreationForm(request.POST,instance=usuario)
        usuario1 = User_normal.objects.get(id_myuser=id_usuario)
        form = forms_user(request.POST,instance=usuario1)
        if form.is_valid():
            form.save()
            return redirect ('view')

    def updateCompany(request , id_usuario):
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 and password2 and password1 != password2:
            raise ValidationError ("La contraseña no coincide")
        usuario = Myuser.objects.get(pk=id_usuario)
        form = UserCreationForm(request.POST,instance=usuario)
        usuario1 = Company.objects.get(id_myuser=id_usuario)
        form = forms_company(request.POST,instance=usuario1)
        if form.is_valid():
            form.save()
            return redirect ('view')

    def deleteUsuario(request, id_usuario):
        user=Myuser.objects.get(pk=id_usuario)
        user.delete()
        if user.type_user == 'User':
            user1=User_normal.objects.get(id_myuser = id_usuario)
            user1.delete()
        elif user.type_user == 'Superuser':
            raise ValidationError ('No se puede eliminar Superusuarios')
        else:
            user2 = Company.objects.get (id_myuser = id_usuario)
            user2.delete()
        return redirect ('view')
