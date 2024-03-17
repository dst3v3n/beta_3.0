from django.shortcuts import render , redirect
from admins.admin import UserCreationForm
from .forms import forms_user
from admins.models import Myuser
from admins.admin import UserCreationForm
import sweetify
from requisicion.forms import Form_Requi
from admins.forms import Form_Name
from admins.models import Myuser
from company.forms import forms_company
from company.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from HojaVida.mixin import EmailVerificadoMixin
from django.views.generic import TemplateView , ListView
from requisicion.models import Requisicion
from typing import Any
from requisicion.views import ver_requi
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


class visualizar_ofertas (LoginRequiredMixin , EmailVerificadoMixin, ListView):
    model = Requisicion
    template_name = 'ofertazp.html'
    paginate_by = 2

class ver_requi2  (LoginRequiredMixin, ListView):
    model = Requisicion
    queryset = Requisicion.objects.all()
    template_name = 'verrequiusu.html'
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        form_requi = Form_Requi(instance=Requisicion.objects.get(id_myuser = self.kwargs['id_myuser']))
        form_admin = Form_Name (instance= Myuser.objects.get(pk=self.request.COOKIES.get('User_id')))
        form_comp = forms_company (instance= Company.objects.get(id_myuser_id=self.request.COOKIES.get('User_id')))
        context['form_requi'] = form_requi
        context['form_name'] = form_admin
        context['forms_company'] = form_comp
        return context