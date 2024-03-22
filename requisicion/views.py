from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from .forms import Form_Requi , Form_Habi_Requi
from admins.forms import Form_Name
from admins.models import Myuser
from company.forms import forms_company
from company.models import Company
from .alerta import alertas
from django.contrib.auth.mixins import LoginRequiredMixin
from HojaVida.mixin import EmailVerificadoMixin
from django.views.generic import TemplateView , ListView , View
from .models import Requisicion , Habilidades_requi , Ponderacion

# Create your views here.

class create_oferta (LoginRequiredMixin , EmailVerificadoMixin, TemplateView):

    template_name = 'crearrequisicion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_requi = Form_Requi ()
        form_admin = Form_Name (instance= Myuser.objects.get(pk=self.request.COOKIES.get('User_id')))
        form_comp = forms_company (instance= Company.objects.get(id_myuser_id=self.request.COOKIES.get('User_id')))
        list_habi = [Form_Habi_Requi(prefix = "formulario00")]

        data = {
            'form_requi': form_requi,
            'form_habi': list_habi,
            'form_name' : form_admin,
            'form_company' : form_comp,
            'in_habi' : (Form_Habi_Requi (prefix = 'formulario1'))
        }
        context.update(data)
        return context


class save_requi:

    def edit_requi (request , id):
        if request.method == 'POST':
            usuario = Requisicion.objects.get (pk = id)
            form = Form_Requi (request.POST , instance= usuario)
            if form.is_valid ():
                form.save ()
                return redirect ('ver_oferta' , id_myuser = request.user.id)

class consultar_ofer (LoginRequiredMixin , EmailVerificadoMixin, ListView):
    model = Requisicion
    template_name = 'veroferta.html'
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(id_myuser_id=self.kwargs['id_myuser'])
        return qs


class ver_requi (LoginRequiredMixin , EmailVerificadoMixin, TemplateView):

    template_name = 'verrequisicion.html'

    def get_queryset(self):

        return Ponderacion.objects.order_by('total', '-total')

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        form_requi = Form_Requi(instance=Requisicion.objects.get(id = self.kwargs['id_oferta']))
        form_admin = Form_Name (instance= Myuser.objects.get(pk=self.request.COOKIES.get('User_id')))
        form_comp = forms_company (instance= Company.objects.get(id_myuser_id=self.request.COOKIES.get('User_id')))
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

        data = {
            'form_requi' : form_requi,
            'form_name' : form_admin,
            'form_company' : form_comp,
            'form_habi' : list_habi,
            'ponderacion' : self.get_queryset(),
            'in_habi' : (Form_Habi_Requi (prefix = 'formulario1'))
            }
        context.update (data)
        return context

class save_form (View):

    def post(self, request, *args, **kwargs):
        form_requi = Form_Requi(self.request.POST)
        if form_requi.is_valid():
            info1 = form_requi.save(commit=False)
            info1.id_myuser_id  = self.request.COOKIES.get('User_id')
            info1.save()

        for i in range (20):
            form = Form_Habi_Requi(self.request.POST , prefix = f'formulario{i}')
            print(form)
            if form.is_valid():
                info = form.save(commit=False)
                info.id_myuser_id  = self.request.COOKIES.get('User_id')
                info.id_requi_id  = info1.id
                info.save()
            else:
                if i > 0:
                    return redirect ('create_oferta')

        return redirect ('create_oferta')

class delete_requi (View):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        Requisicion.objects.get (pk = self.kwargs["id_requisicion"]).delete ()
        return redirect ('consultar_ofer' , id_myuser = self.request.user.id)
