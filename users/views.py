from django.http import HttpRequest
from django.shortcuts import render , redirect
from django.urls import reverse
from admins.admin import UserCreationForm
from .forms import forms_user
from admins.models import Myuser
from admins.admin import UserCreationForm
import sweetify
from .ponderacion import ubicacion , experiencia , educacion
from requisicion.forms import Form_Requi , Form_Habi_Requi
from admins.forms import Form_Name
from admins.models import Myuser
from company.forms import forms_company
from company.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from HojaVida.mixin import EmailVerificadoMixin
from django.views.generic import TemplateView , ListView
from requisicion.models import Requisicion , Ponderacion , Habilidades_requi
from HojaVida.models import Personal_information , Education , Experience
from typing import Any
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

class ver_requi2  (LoginRequiredMixin , EmailVerificadoMixin , TemplateView):

    template_name = 'verrequiusu.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        form_requi = Form_Requi(instance = Requisicion.objects.get(pk = self.kwargs['id_oferta']))
        form_admin = Form_Name (instance = Myuser.objects.get(pk = self.request.COOKIES.get('User_id')))
        form_comp = forms_company (instance = Company.objects.get(id_myuser_id = self.kwargs['id_myuser']))

        list_habi = []
        instancia_0 = Habilidades_requi.objects.filter(id_requi_id  = self.kwargs['id_oferta']).values ()
        if len(instancia_0) >= 1:
            for i in instancia_0:
                id_habilidades = i['id']
                x =Habilidades_requi.objects.get(id = id_habilidades)
                form_habi_instance = Form_Habi_Requi (instance= x)
                list_habi.append(form_habi_instance)
        else:
            list_habi.append (Form_Habi_Requi (prefix = 'formulario0'))

        if not Personal_information.objects.filter(id_myuser_id = self.request.user.id).exists():
            return redirect ("create_hoja")

        personal = Personal_information.objects.filter(id_myuser_id = self.request.user.id).values("address" , "city")
        company = Requisicion.objects.filter (id = self.kwargs['id_oferta']). values ("direccion" , "ciudad")
        distancia_user = f"{personal[0]["address"]}, {personal[0]["city"]}"
        distancia_company = f"{company[0]["direccion"]}, {company[0]["ciudad"]}"

        # distancia = ubicacion(distancia_user , distancia_company)

        meses_experiencia = experiencia(self.request.user.id , self.kwargs['id_oferta'])
        # educacion1 = educacion(self.kwargs['id_oferta'] , self.request.user.id )
        data = {
            'form_requi' : form_requi,
            'form_name' : form_admin,
            'form_company' : form_comp,
            'distancia' : 30,
            'educacion' : 30,
            'habilidades' : 30,
            'id_myuser_oferta' : self.kwargs['id_myuser'],
            'form_habi' : list_habi,
            'experiencia' : meses_experiencia,
        }

        return render(request, self.template_name, data)



class postulacion (LoginRequiredMixin , EmailVerificadoMixin , TemplateView):

    template_name = 'verrequiusu.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        if self.request.method == 'POST':
            educacion =  float(self.request.POST["educacion"].replace(',', '.'))
            experiencia = float(self.request.POST["experiencia"].replace(',', '.'))
            distancia = float(self.request.POST["distancia"].replace(',', '.'))
            habilidades = float(self.request.POST["habilidades"].replace(',', '.'))
            oferta = self.request.POST["id_oferta"]
            id_myuser_oferta = self.request.POST["id_oferta_myuser"]
            total = (educacion+experiencia+distancia+habilidades)*30/10
            Ponderacion(educacion=educacion , experiencia=experiencia , habilidades=habilidades , ubicacion=distancia , total=total , id_oferta_id= oferta , id_myuser_id=self.request.user.id).save()
        return redirect ('ver_info_ofertas' , id_oferta = oferta , id_myuser = id_myuser_oferta)
