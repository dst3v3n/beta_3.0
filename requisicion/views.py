from django.shortcuts import render , redirect
from .forms import Form_Requi
from admins.forms import Form_Name
from admins.models import Myuser
from company.forms import forms_company
from company.models import Company
from .alerta import alertas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from HojaVida.mixin import EmailVerificadoMixin
from django.views.generic import TemplateView , ListView
from .models import Requisicion

# Create your views here.

class vista:
    def ver(request):
        return render (request, 'veroferta.html')


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
            'form_company' : form_comp
        }
        context.update(data)
        return context


class save_requi:

    def info_requi (request):
        if request.method == 'POST':
            print("hola")
            form = Form_Requi (request.POST)
            if form.is_valid() :
                print("hola")
                info = form.save(commit = False)
                id_company = Company.objects.filter(id_myuser_id = request.COOKIES.get('User_id')).values ()
                info.id_company_id = id_company[0]["id"]
                info.save ()
                alertas.save (request , 'Informacion Personal')
                return redirect ('create_oferta')

class consultar_ofer (LoginRequiredMixin , EmailVerificadoMixin, ListView):
    model = Requisicion
    template_name = 'veroferta.html'
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(id_company__id=self.kwargs['company_id'])
        return qs