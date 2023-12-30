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

class Form_Name (forms.ModelForm):
    class Meta:
        model = Myuser
        fields = ['name' , 'email']

        widgets = {
            'email': forms.TextInput(attrs={'class': 'inp'}),
            'name': forms.TextInput(attrs={'class': 'inp'}),
                }
