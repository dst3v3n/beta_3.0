from django.shortcuts import render , redirect
from . forms import Form_Requi
from admins.forms import Form_Name
from admins.models import Myuser
from company.forms import forms_company
from company.models import Company
from .alerta import alertas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .mixin import EmailVerificadoMixin
from django.views.generic import TemplateView

# Create your views here.

class vista:
    def ver(request):
        return render (request, 'verrequisicion.html')


class create_oferta (LoginRequiredMixin , EmailVerificadoMixin, TemplateView):

    template_name = 'crearrequisicion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_admin = Form_Name (instance= Myuser.objects.get(pk=self.request.COOKIES.get('User_id')))
        form_comp = forms_company (instance= Company.objects.get(id_myuser_id=self.request.COOKIES.get('User_id')))
        data = {
            'form_requi': Form_Requi (),
            'form_name' : form_admin,
            'form_company' : form_comp
        }
        context.update(data)
        return context


class save_requi:
    def info_requi (request):
        if request.method == 'POST':
            form1 = Form_Requi (request.POST)
            print(form1)
            print("hola")

            if form1.is_valid():
                info = form1.save(commit = False)
                hola = Company.objects.filter(id_myuser_id = request.COOKIES.get('User_id')).first ()
                print(hola)
                info.id_myuser_id  = request.COOKIES.get ('User_id')
                # info.id_company_id = Company.objects.filter()
                # info.save ()
                alertas.save (request , 'Requisicion')
                return redirect ('create_oferta')