from django.shortcuts import render , redirect
from . forms import Form_Requi
from .models import Requisicion
from admins.models import Myuser
from admins.forms import Form_Name
from users.models import User_normal
from users.forms import forms_user
from django.contrib.auth.decorators import login_required
from pathlib import Path
from .alerta import alertas
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .mixin import EmailVerificadoMixin
from django.views.generic import View , TemplateView

# Create your views here.
class create_oferta (LoginRequiredMixin , EmailVerificadoMixin, TemplateView):

    template_name = 'crearrequisicion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_requi = []
        instancia_2 = Requisicion.objects.filter(id_myuser_id  = self.request.COOKIES.get('User_id')).values ()
        if len(instancia_2) == 2:
            for i in instancia_2:
                id_person = i['id']
                x = Requisicion.objects.get(id = id_person)
                form_requisi = Form_Requi (instance = x)
                list_requi.append(form_requisi)

        elif len(instancia_2) == 1:
            for i in instancia_2:
                id_person = i['id']
                x = Requisicion.objects.get(id = id_person)
                form_requisi = Form_Requi (instance = x , prefix = 'formulario1')
                list_requi.append(form_requisi)
                list_requi.append(Form_Requi (prefix = 'formulario2'))
                pass

        else:
            list_requi = [Form_Requi (prefix = 'formulario1') , Form_Requi (prefix = 'formulario2') ]

        data = {
            'form_requi': list_requi
        }

        context.update(data)
        return context


class save_requi:

    def info_requi (request):
        if request.method == 'POST':
            form2 = Form_Requi (request.POST)
            if form2.is_valid() :
                info = form2.save(commit = False)
                info.id_myuser_id  = request.COOKIES.get ('User_id')
                info.save ()
                alertas.save (request , 'Requisicion')
                return redirect ('create_oferta')