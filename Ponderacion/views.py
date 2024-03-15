from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from HojaVida.mixin import EmailVerificadoMixin
from django.views.generic import ListView

# Create your views here.

class User_ponderacion (LoginRequiredMixin , EmailVerificadoMixin , ListView):
    
    template_name = "veroferta.html"