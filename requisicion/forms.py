from django import forms
from . models import Requisicion

class Date (forms.DateInput):
    input_type = 'date'

class Form_Requi (forms.ModelForm):
    class Meta:
        model = Requisicion
        fields = ['date_inicio' , 'date_fin', 'company_name' , 'location' ,'nit','ubication','codigo_cno','cell_number','name_cargo','nivel_edu','type_contrato','type_salario','experiencia','habilidades','salario','jornada_laboral','descripcion']
        widgets = {
            'date_inicio' : Date (attrs={'class': 'inp2'}),
            'date_fin' : Date (attrs={'class': 'inp2'}),
            'company_name' : forms.TextInput (attrs={'class': 'inp' , "required" : False}),
            'location' : forms.TextInput (attrs={'class' : 'inp' , "required" : False}),
            'nit' : forms.TextInput (attrs={'class' : 'inp' , "required" : False}),
            'ubication' : forms.TextInput (attrs={'class' : 'inp' , "required" : False}),
            'codigo_cno' : forms.TextInput (attrs={'class' : 'inp' , "required" : False}),
            'cell_number' : forms.TextInput (attrs={'class': 'inp1' , "required" : False}),
            'name_cargo' : forms.TextInput (attrs={'class': 'inp',}),
            'nivel_edu': forms.Select(attrs={'class': 'inp2'}),
            'type_contrato': forms.Select(attrs={'class': 'inp2'}),
            'type_salario' : forms.TextInput (attrs={'class': 'inp',}),
            'experiencia' : forms.TextInput (attrs={'class': 'inp',}),
            'habilidades' : forms.TextInput (attrs={'class': 'inp',}),
            'salario' : forms.TextInput (attrs={'class': 'inp',}),
            'jornada_laboral' : forms.TextInput (attrs={'class': 'inp',}),
            'descripcion' : forms.TextInput (attrs={'class': 'inp',}),
        }
        
