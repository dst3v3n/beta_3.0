from django import forms
from .models import User_normal

class forms_user (forms.ModelForm):

    class Meta:
        model = User_normal
        fields = ['last_name']
