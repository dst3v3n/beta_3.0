from django import forms
from . models import Requisicion
from datetime import date, timedelta

fecha_hoy = date.today()

fecha_minima = fecha_hoy + timedelta(days=5)
fecha_maxima = fecha_hoy + timedelta(days=31)

fecha_minima.strftime('%Y-%m-%d')
fecha_maxima.strftime('%Y-%m-%d')

class Date (forms.DateInput):
    input_type = 'date'

class Form_Requi (forms.ModelForm):
    class Meta:
        model = Requisicion
        fields = ['fecha_inicio','fecha_finalizacion','direccion','departamento','ciudad','telefono','codigo_cno',
                  'nombre_cargo','educacion','experiencia_laboral','profesion','habilidades','salario','forma_pago',
                  'jornada_laboral','tipo_contrato','descripcion']
        # fields = "__all__"

        widgets = {
            'fecha_inicio': Date (attrs={'class': 'inp3',
                                         'max' : fecha_minima.strftime('%Y-%m-%d'),
                                         'min' : fecha_hoy.strftime('%Y-%m-%d')}),
            'fecha_finalizacion': Date (attrs={'class': 'inp3',
                                               'max' : fecha_maxima.strftime('%Y-%m-%d'),
                                               'min' : fecha_hoy.strftime('%Y-%m-%d')
                                            }),
            'direccion':forms.TextInput (attrs={'class' : 'inp2'}),
            'departamento': forms.TextInput (attrs={'class' : 'inp2'}),
            'ciudad': forms.TextInput (attrs={'class' : 'inp2'}),
            'telefono': forms.TextInput (attrs={'class': 'inp3'}),
            'codigo_cno': forms.NumberInput (attrs={'class' : 'inp3'}),
            'nombre_cargo':forms.TextInput (attrs={'class': 'inp2',}),
            'educacion':forms.Select(attrs={'class': 'inp2'}),
            'experiencia_laboral': forms.TextInput (attrs={'class': 'inp3',}),
            'profesion':forms.TextInput (attrs={'class': 'inp2',}),
            'salario':forms.NumberInput (attrs={'class': 'inp3',
                                              'step': 0.50}),
            'forma_pago': forms.Select (attrs={'class': 'inp3',}),
            'jornada_laboral': forms.TextInput (attrs={'class': 'inp3',}),
            'tipo_contrato':forms.Select(attrs={'class': 'inp3'}),
            'descripcion': forms.Textarea (attrs={'id': 'infoa'}),
            'habilidades': forms.Textarea (attrs={'class': 'inth',}),
        }
