from django import forms
from . models import Personal_information , Education , Experience , Personal_references , Business_references , Additional_information

class Date (forms.DateInput):
    input_type = 'date'

class Form_Person_Info (forms.ModelForm):

    class Meta:
        model = Personal_information
        fields = ['address' , 'cell_phone' , 'date' , 'type_d' , 'n_document' , 'gender' , 'age' , 'civil']

        widgets = {
            'address': forms.TextInput(attrs={'class': 'inp'}),
            'cell_phone' : forms.TextInput (attrs={'class': 'inp1'}),
            'date' : Date (attrs={'class': 'inp2'}),
            'type_d': forms.Select(attrs={'class': 'inp2'}),
            'n_document' : forms.TextInput (attrs={'class': 'inp1'}),
            'gender': forms.Select(attrs={'class': 'inp2'}),
            'age': forms.NumberInput(attrs={'class': 'inp1'}),
            'civil': forms.Select(attrs={'class': 'inp2'}),
        }

class Form_Education (forms.ModelForm):
    class Meta:
        model = Education
        fields = ['archive' , 'name_institution' , 'graduation_year' , 'time' ]
        widgets = {
            'archive' : forms.FileInput (attrs={'class': 'inp3',
                                                'accept' : '.pdf',
                                                'id' : 'img',
                                                'required' : False
                                                }),
            'name_institution' : forms.TextInput (attrs={'class' : 'inp'}),
            'graduation_year' : Date (attrs={'class': 'inp2'}),
            'time' : forms.NumberInput (attrs= {'class' : 'inp1',
                                                'Placeholder' : 'Introduzca el número de meses',}),
        }

class Form_Experience (forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company_name' , 'company_position' , 'start_date' , 'end_date' , 'functions']
        widgets = {
            'company_name' : forms.TextInput (attrs={'class': 'inp',}),
            'company_position' : forms.TextInput (attrs={'class' : 'inp'}),
            'start_date' : Date (attrs={'class': 'inp2'}),
            'end_date' : Date (attrs={'class': 'inp2'}),
            'functions' : forms.Textarea (attrs= {'id' : 'dsr'}),
        }

class Form_Person_Refe (forms.ModelForm):
    class Meta:
        model = Personal_references
        fields = ['person_name' , 'last_person_name' , 'address' , 'cell_number']
        widgets = {
            'person_name' : forms.TextInput (attrs={'class': 'inp',}),
            'last_person_name' : forms.TextInput (attrs={'class' : 'inp'}),
            'address' : forms.TextInput (attrs={'class' : 'inp'}),
            'cell_number' : forms.NumberInput (attrs={'class': 'inp1'}),
        }

class Form_Business_Refe (forms.ModelForm):
    class Meta:
        model = Business_references
        fields = ['company_name' , 'boss_name' , 'address' , 'cell_number']
        widgets = {
            'company_name' : forms.TextInput (attrs={'class': 'inp' , "required" : False}),
            'boss_name' : forms.TextInput (attrs={'class' : 'inp' , "required" : False}),
            'address' : forms.TextInput (attrs={'class' : 'inp' , "required" : False}),
            'cell_number' : forms.NumberInput (attrs={'class': 'inp1' , "required" : False}),
        }

class Form_Aditional (forms.ModelForm):
    class Meta:
        model= Additional_information
        fields = ['information_adi']
        widgets = {
            'information_adi' : forms.Textarea (attrs= {'id' : 'infoa'}),
        }
