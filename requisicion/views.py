from typing import Any
from django.shortcuts import redirect
from .forms import Form_Requi
from admins.forms import Form_Name
from admins.models import Myuser
from company.forms import forms_company
from company.models import Company
from .alerta import alertas
from django.contrib.auth.mixins import LoginRequiredMixin
from HojaVida.mixin import EmailVerificadoMixin
from django.views.generic import TemplateView , ListView
from .models import Requisicion

# Create your views here.

class create_oferta (LoginRequiredMixin , EmailVerificadoMixin, TemplateView):

    template_name = 'crearrequisicion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_requi = Form_Requi ()
        form_admin = Form_Name (instance= Myuser.objects.get(pk=self.request.COOKIES.get('User_id')))
        form_comp = forms_company (instance= Company.objects.get(id_myuser_id=self.request.COOKIES.get('User_id')))

        data = {
            'form_requi': form_requi,
            'form_name' : form_admin,
            'form_company' : form_comp,
        }
        context.update(data)
        return context


class save_requi:

    def info_requi (request):
        if request.method == 'POST':
            form = Form_Requi (request.POST)
            if form.is_valid() :
                info = form.save(commit = False)
                info.id_myuser_id = request.COOKIES.get('User_id')
                info.save ()
                alertas.save (request , 'Informacion Personal')
                return redirect ('create_oferta')


    def edit_requi (request , id):
        if request.method == 'POST':
            usuario = Requisicion.objects.get (pk = id)
            form = Form_Requi (request.POST , request.FILES, instance= usuario)
            if form.is_valid ():
                form.save ()
                return redirect ('ver_oferta' , id_myuser = request.user.id)

    def delete_requi (request , id):
        Requisicion.objects.get (pk = id).delete ()
        return redirect ('ver_oferta')

class consultar_ofer (LoginRequiredMixin , EmailVerificadoMixin, ListView):
    model = Requisicion
    template_name = 'veroferta.html'
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(id_myuser_id=self.kwargs['id_myuser'])
        return qs


class ver_requi (LoginRequiredMixin , EmailVerificadoMixin, TemplateView):

    template_name = 'verrequisicion.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        form_requi = Form_Requi(instance=Requisicion.objects.get(id_myuser = self.kwargs['id_myuser']))
        form_admin = Form_Name (instance= Myuser.objects.get(pk=self.request.COOKIES.get('User_id')))
        form_comp = forms_company (instance= Company.objects.get(id_myuser_id=self.request.COOKIES.get('User_id')))
        data = {
            'form_requi' : form_requi,
            'form_name' : form_admin,
            'form_company' : form_comp,
            }
        context.update (data)
        return context
