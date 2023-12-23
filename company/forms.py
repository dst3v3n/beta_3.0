from django import forms
from .models import Company

class forms_company (forms.ModelForm):

    class Meta:
        model = Company
        fields = ['nit']
