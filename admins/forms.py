from django import forms
from .models import Myuser

class Form_Acceso (forms.Form):
    email = forms.EmailField (label = "email" , widget=forms.EmailInput(attrs={
        'Placeholder' : 'Digite su correo',
        'required' : True,
    }))
    password = forms.CharField (label = "password" , widget=forms.PasswordInput(attrs={
        'Placeholder' : 'Digite su contraseña',
        'id' : 'passw',
        'class' : 'pass'
    }))

class Form_new_user (forms.Form):
    class Meta:
        model = Myuser
        fileds = ['email' , ' name' , 'type_user']
