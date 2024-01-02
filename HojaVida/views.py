from django.shortcuts import render , redirect
from . forms import Form_Person_Info , Form_Education , Form_Experience , Form_Person_Refe , Form_Business_Refe , Form_Aditional
from .models import Personal_information , Education , Experience , Personal_references , Business_references , Additional_information
from admins.models import Myuser
from admins.forms import Form_Name
from users.models import User_normal
from users.forms import forms_user
from django.contrib.auth.decorators import login_required
from pathlib import Path

# Create your views here.

class visualizar:
    @login_required(redirect_field_name="index")
    def create_hoja (request):

        list_educacion = []
        instancia = Education.objects.filter(id_myuser = request.COOKIES.get('User_id')).values ()
        if len(instancia) >= 1:
            for i in instancia:
                id_educacion = i['id']
                x = Education.objects.get(id = id_educacion)
                form_educacion_instance = Form_Education (instance= x)
                list_educacion.append(form_educacion_instance)
        else:
            list_educacion.append (Form_Education (prefix = 'formulario0'))

        list_empresa = []
        instancia_1 = Experience.objects.filter(id_myuser = request.COOKIES.get('User_id')).values ()
        if len(instancia_1) >= 1:
            for i in instancia_1:
                id_empresa = i['id']
                x =Experience.objects.get(id = id_empresa)
                form_empresa_instance = Form_Experience (instance= x)
                list_empresa.append(form_empresa_instance)

        else:
            list_empresa.append (Form_Experience (prefix = 'formulario0'))

        list_personales = []
        instancia_2 = Personal_references.objects.filter(id_myuser = request.COOKIES.get('User_id')).values ()
        if len(instancia_2) == 2:
            for i in instancia_2:
                id_person = i['id']
                x = Personal_references.objects.get(id = id_person)
                form_personales_instance = Form_Person_Refe (instance = x)
                list_personales.append(form_personales_instance)

        elif len(instancia_2) == 1:
            for i in instancia_2:
                id_person = i['id']
                x = Personal_references.objects.get(id = id_person)
                form_personales_instance = Form_Person_Refe (instance = x , prefix = 'formulario1')
                list_personales.append(form_personales_instance)
                list_personales.append(Form_Person_Refe (prefix = 'formulario2'))
                pass

        else:
            list_personales = [Form_Person_Refe (prefix = 'formulario1') , Form_Person_Refe (prefix = 'formulario2') ]

        list_empresariales = []
        instancia_3 = Business_references.objects.filter(id_myuser = request.COOKIES.get('User_id')).values ()
        if len(instancia_3) == 2:
            for i in instancia_3:
                id_person = i['id']
                x = Business_references.objects.get(id = id_person)
                form_empresariales_instance = Form_Business_Refe (instance= x)
                list_empresariales.append(form_empresariales_instance)
        elif len(instancia_3) == 1:
            for i in instancia_3:
                id_person = i['id']
                x = Business_references.objects.get(id = id_person)
                form_empresariales_instance = Form_Business_Refe (instance = x , prefix = 'formulario1')
                list_empresariales.append(form_empresariales_instance)
                list_empresariales.append(Form_Business_Refe (prefix = 'formulario2'))
                pass
        else:
            list_empresariales = [Form_Business_Refe (prefix = 'formulario1') , Form_Business_Refe (prefix = 'formulario2')]

        try:
            form_person = Form_Person_Info (instance = Personal_information.objects.get (id_myuser = request.COOKIES.get ('User_id')))
        except:
            form_person = Form_Person_Info ()
        try:
            form_aditional = Form_Aditional (instance = Additional_information.objects.get (id_myuser = request.COOKIES.get ('User_id')))
        except:
            form_aditional = Form_Aditional ()

        data =  {
                'form_name' : Form_Name (instance = Myuser.objects.get(pk = request.COOKIES.get ('User_id'))),
                'form_last' : forms_user (instance = User_normal.objects.get (id_myuser = request.COOKIES.get ('User_id'))),
                'form_info' : form_person,
                'form_edu' : list_educacion,
                'form_empresa' : list_empresa,
                'form_person_refe' : list_personales,
                'form_empresarial_refe' : list_empresariales,
                'form_adicio' : form_aditional,
                'in_edu' : Form_Education (prefix = 'formulario1') ,
                'in_exp' : Form_Experience (prefix = 'formulario1') ,
                }

        return render (request , 'hoja_vida.html' , data)

    @login_required(redirect_field_name="index")
    def view_hoja (request):
        list_educacion = []
        instancia = Education.objects.filter(id_myuser = request.COOKIES.get('User_id')).values ()
        if len(instancia) >= 1:
            for i in instancia:
                id_educacion = i['id']
                x = Education.objects.get(id = id_educacion)
                form_educacion_instance = Form_Education (instance= x)
                list_educacion.append(form_educacion_instance)
        else:
            list_educacion.append (Form_Education ())

        list_empresa = []
        instancia_1 = Experience.objects.filter(id_myuser = request.COOKIES.get('User_id')).values ()
        if len(instancia_1) >= 1:
            for i in instancia_1:
                id_empresa = i['id']
                x =Experience.objects.get(id = id_empresa)
                form_empresa_instance = Form_Experience (instance= x)
                list_empresa.append(form_empresa_instance)
        else:
            list_empresa.append (Form_Experience ())

        list_personales = []
        instancia_2 = Personal_references.objects.filter(id_myuser = request.COOKIES.get('User_id')).values ()
        if len(instancia_2) == 1:
            for i in instancia_2:
                id_person = i['id']
                x = Personal_references.objects.get(id = id_person)
                form_personales_instance = Form_Person_Refe (instance = x)
                list_personales.append(form_personales_instance)
        else:
            list_personales = [Form_Person_Refe (prefix = 'formulario1') , Form_Person_Refe (prefix = 'formulario2') ]

        list_empresariales = []
        instancia_3 = Business_references.objects.filter(id_myuser = request.COOKIES.get('User_id')).values ()
        if len(instancia_3) >= 1:
            for i in instancia_3:
                id_person = i['id']
                x = Business_references.objects.get(id = id_person)
                form_empresariales_instance = Form_Business_Refe (instance= x)
                list_empresariales.append(form_empresariales_instance)
        else:
            list_empresariales = [Form_Business_Refe (prefix = 'formulario1') , Form_Business_Refe (prefix = 'formulario2')]

        try:
            form_person = Form_Person_Info (instance = Personal_information.objects.get (id_myuser = request.COOKIES.get ('User_id')))
        except:
            form_person = Form_Person_Info ()
        try:
            form_aditional = Form_Aditional (instance = Additional_information.objects.get (id_myuser = request.COOKIES.get ('User_id')))
        except:
            form_aditional = Form_Aditional ()

        data =  {
                'form_name' : Form_Name (instance = Myuser.objects.get(pk = request.COOKIES.get ('User_id'))),
                'form_last' : forms_user (instance = User_normal.objects.get (id_myuser = request.COOKIES.get ('User_id'))),
                'form_info' : form_person,
                'form_edu' : list_educacion,
                'form_empresa' : list_empresa,
                'form_person' : list_personales,
                'form_empresarial' : list_empresariales,
                'form_adicio' : form_aditional,
                }
        return render (request , 'hoja_vida_visualizar.html' , data)

class save_hj:

    def save_info (request):
        if request.method == 'POST':
            form2 = Form_Person_Info (request.POST)
            if form2.is_valid() :
                info = form2.save(commit = False)
                info.id_myuser = request.COOKIES.get ('User_id')
                info.save ()
                return redirect ('create_hoja')

    def save_education (request):
        if request.method == 'POST':
            for i in range (20):
                form = Form_Education(request.POST , request.FILES , prefix = f'formulario{i}')
                if form.is_valid():
                    info = form.save(commit=False)
                    info.id_myuser = request.COOKIES.get('User_id')
                    info.save()
                # else:
                #     return redirect ('create_hoja')
            return redirect ('create_hoja')

    def save_experience (request):
        if request.method == 'POST':
            for i in range (20):
                form = Form_Experience(request.POST , prefix = f'formulario{i}')
                if form.is_valid():
                    info = form.save(commit=False)
                    info.id_myuser = request.COOKIES.get('User_id')
                    info.save()
                else:
                    return redirect ('create_hoja')
            return redirect ('create_hoja')

    def save_reference (request):
        if request.method == 'POST':
            form1 = Form_Person_Refe (request.POST , prefix = 'formulario1')
            form2 = Form_Person_Refe (request.POST , prefix = 'formulario2')
            getlist = request.POST.getlist('formulario1-last_person_name')
            getlist1 = request.POST.getlist('formulario2-last_person_name')
            if not (getlist[0] == ""):
                if len(Personal_references.objects.filter(id_myuser = request.COOKIES.get('User_id'))) < 1:
                    if form1.is_valid () :
                        info1 = form1.save(commit=False)
                        info1.id_myuser = request.COOKIES.get('User_id')
                        info1.save()

            if not (getlist1[0] == ""):
                if form2.is_valid () :
                    info2 = form2.save(commit=False)
                    info2.id_myuser = request.COOKIES.get('User_id')
                    info2.save()


            form3 = Form_Business_Refe (request.POST , prefix = 'formulario1')
            form4 = Form_Business_Refe (request.POST , prefix = 'formulario2')
            getlist = request.POST.getlist('formulario1-company_name')
            getlist1 = request.POST.getlist('formulario2-company_name')


            if not (getlist[0] == ""):
                if len(Business_references.objects.filter(id_myuser = request.COOKIES.get('User_id'))) < 1:
                    if form3.is_valid () :
                        info3 = form3.save(commit=False)
                        info3.id_myuser = request.COOKIES.get('User_id')
                        info3.save ()
            if not (getlist1[0] == ""):
                if form4.is_valid () :
                    info4 = form4.save(commit=False)
                    info4.id_myuser = request.COOKIES.get('User_id')
                    info4.save ()
            return redirect ('create_hoja')

    def save_aditional (request):
        if request.method == 'POST':
            form1 = Form_Aditional (request.POST)
            if form1.is_valid () :
                info1 = form1.save(commit=False)
                info1.id_myuser = request.COOKIES.get('User_id')
                info1.save ()
            return redirect ('create_hoja')

    def edit_information  (request):
        if request.method == 'POST':
            informacion = Personal_information.objects.get (id_myuser = request.COOKIES.get ('User_id'))
            informacion2 = User_normal.objects.get (id_myuser = request.COOKIES.get ('User_id'))
            form = Form_Person_Info (request.POST , instance = informacion)
            form1 = Form_Name (request.POST , instance = Myuser.objects.get(pk = request.COOKIES.get ('User_id')))
            form2 = forms_user (request.POST , instance = informacion2)

            if form.is_valid ():
                form.save ()

            if form1.is_valid ():
                form1.save ()

            if form2.is_valid ():
                form2.save ()
            return redirect ('create_hoja')

    def edit_education (request , id_usuario):
        if request.method == 'POST':
            usuario = Education.objects.get (pk = id_usuario)
            form = Form_Education (request.POST, request.FILES, instance= usuario)
            if form.is_valid ():
                form.save ()
                return redirect ('create_hoja')

    def edit_experience (request , id_usuario):
        if request.method == 'POST':
            usuario = Experience.objects.get (pk = id_usuario)
            form = Form_Experience (request.POST , instance= usuario)
            if form.is_valid ():
                form.save ()
                return redirect ('create_hoja')

    def edit_personal_reference (request , id_usuario):
        if request.method == 'POST':
            usuario = Personal_references.objects.get (pk = id_usuario)
            form = Form_Person_Refe (request.POST , instance= usuario)
            if form.is_valid ():
                form.save ()
                return redirect ('create_hoja')

    def edit_bussiness_reference (request , id_usuario):
        if request.method == 'POST':
            usuario = Personal_references.objects.get (pk = id_usuario)
            form = Form_Person_Refe (request.POST , instance= usuario)
            if form.is_valid ():
                form.save ()
                return redirect ('create_hoja')

    def edit_aditional (request):
        if request.method == 'POST':
            informacion = Additional_information.objects.filter(id_myuser = request.COOKIES.get ('User_id')).first()
            form = Form_Aditional(request.POST , instance=informacion)
            if form.is_valid():
                form.save()
                return redirect ('create_hoja')

    def delete_information (request):
        Personal_information.objects.get (id_myuser = request.COOKIES.get('User_id')).delete ()
        return redirect ('create_hoja')

    def delete_education (request , id_usuario):
        pdf = Education.objects.get(pk = id_usuario)
        url = pdf.archive.url
        filePath = Path(f'D:\\Steven\Git_Steven\\beta_3.0{url}')
        if filePath.exists () :
            filePath.unlink ()
            Education.objects.get (pk = id_usuario).delete ()
            return redirect ('create_hoja')

    def delete_experience (request , id_usuario):
        Experience.objects.get (pk = id_usuario).delete ()
        return redirect ('create_hoja')

    def delete_personal_reference (request , id_usuario):
        Personal_references.objects.get (pk = id_usuario).delete ()
        return redirect ('create_hoja')

    def delete_bussiness_reference (request , id_usuario):
        Business_references.objects.get (pk = id_usuario).delete ()
        return redirect ('create_hoja')

    def delete_aditional (request):
        Additional_information.objects.get (id_myuser = request.COOKIES.get('User_id')).delete ()
        return redirect ('create_hoja')
