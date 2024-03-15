from django import forms
from . models import Perfil

class Date (forms.DateInput):
    input_type = 'date'

class Form_Info_Perfil (forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        widgets = {
            
            'Direccion': forms.TextInput(attrs={'class': 'perf'}),
            'Telefono' : forms.NumberInput (attrs={'class': 'perf1'}),
            'Profesion': forms.TextInput(attrs={'class': 'perf'}),
            'Cargo': forms.TextInput(attrs={'class': 'perf'}),
            'Ubicacion': forms.TextInput(attrs={'class': 'perf'}),
            'Fecha_nacimiento' : forms.DateInput (attrs={'class': 'perf2'}),
            'Registro' : forms.DateTimeInput (attrs={'class': 'perf2'}),
            'Redes_sociales': forms.URLInput(attrs={'class': 'perf3'}),
            'Fondo': forms.FileInput(attrs={'class': 'fondo_per4'}),
            'Foto_perfil': forms.FileInput(attrs={'class': 'foto_per4'}),
        }