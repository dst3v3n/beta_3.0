from django import forms
from . models import Requisicion

class Date (forms.DateInput):
    input_type = 'date'

class Form_Requi (forms.ModelForm):
    class Meta:
        model = Requisicion
        fields = ['fecha_inicio','fecha_finalizacion','direccion','departamento','telefono','codigo_cno','nombre_cargo','educacion','experiencia_laboral','habilidades','salario','forma_pago','jornada_laboral','tipo_contrato','descripcion']
        widgets = {
            'fecha_inicio': Date (attrs={'class': 'inp3'}),
            'fecha_finalizacion': Date (attrs={'class': 'inp3'}),
            'direccion':forms.TextInput (attrs={'class' : 'inp2'}),
            'departamento': forms.TextInput (attrs={'class' : 'inp2'}),
            'telefono': forms.TextInput (attrs={'class': 'inp3'}),
            'codigo_cno': forms.TextInput (attrs={'class' : 'inp3'}),
            'nombre_cargo':forms.TextInput (attrs={'class': 'inp2',}),
            'educacion':forms.Select(attrs={'class': 'inp2'}),
            'experiencia_laboral': forms.TextInput (attrs={'class': 'inp3',}),
            'habilidades': forms.TextInput (attrs={'class': 'inp3',}),
            'salario':forms.TextInput (attrs={'class': 'inp3',}),
            'forma_pago': forms.Select (attrs={'class': 'inp3',}),
            'jornada_laboral': forms.TextInput (attrs={'class': 'inp3',}),
            'tipo_contrato':forms.Select(attrs={'class': 'inp3'}),
            'descripcion': forms.TextInput (attrs={'id': 'infoa',
                                                   'style' : "height: 300px;width: 35%; margin-left:33%; border-radius:5%;",
                                                   'rows':"10",
                                                   'cols':"40"}),
        }
