from django.db import models
from . select import Informacion_Per

# Create your models here.

class Personal_information (models.Model):
    address = models.CharField (max_length = 100)
    cell_phone = models.CharField (max_length = 11)
    date = models.DateField ()
    type_d = models.CharField (max_length = 50 , choices=Informacion_Per.documento() , default = 'Cedula Ciudadania')
    n_document = models.CharField (max_length = 15)
    gender = models.CharField (max_length = 50 , choices=Informacion_Per.genero() , default = 'Masculino')
    age = models.IntegerField ()
    civil = models.CharField (max_length = 50 , choices=Informacion_Per.estado_civil() , default = 'Soltero')
    id_myuser = models.PositiveIntegerField (null=True , unique = True)

    class Meta:
        verbose_name = 'Personal_information'
        verbose_name_plural = 'Personal_information'
        db_table = 'Personal_information'

    def __str__(self):
        return f"{self.address}"

class Education (models.Model):
    archive = models.FileField (upload_to='Archivo_Educacion')
    name_institution = models.CharField (max_length = 50)
    graduation_year = models.DateField ()
    time = models.IntegerField ()
    id_myuser = models.PositiveIntegerField (null=True)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        db_table = 'Education'

    def __str__(self):
        return f"{self.name_institution}"

class Experience (models.Model):
    company_name = models.CharField (max_length = 50)
    company_position = models.CharField (max_length = 50)
    start_date = models.DateField ()
    end_date = models.DateField ()
    functions = models.TextField (null=True , blank=True)
    id_myuser = models.PositiveIntegerField (null=True)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        db_table = 'Experience'

    def __str__(self):
        return f"{self.company_name}"

class Personal_references (models.Model):
    person_name = models.CharField (max_length = 50)
    last_person_name = models.CharField (max_length = 50)
    address = models.CharField (max_length = 50)
    cell_number = models.IntegerField ()
    id_myuser = models.PositiveIntegerField (null=True)

    class Meta:
        verbose_name = 'personal_references'
        verbose_name_plural = 'personal_references'
        db_table = 'personal_references'

    def __str__(self):
        return f"{self.person_name}"

class Business_references (models.Model):
    company_name = models.CharField (max_length = 50 , blank=True , null=False)
    boss_name = models.CharField (max_length = 50, blank=True , null=False)
    address = models.CharField (max_length = 50 , blank=True , null=False)
    cell_number = models.IntegerField (blank=True , null=False)
    id_myuser = models.PositiveIntegerField (blank=True , null=True)

    class Meta:
        verbose_name = 'business_references'
        verbose_name_plural = 'business_references'
        db_table = 'business_references'

    def __str__(self):
        return f"{self.company_name}"

class Additional_information (models.Model):
    information_adi = models.TextField ()
    id_myuser = models.PositiveIntegerField (null=True , unique = True)

    class Meta:
        verbose_name = 'additional_information'
        verbose_name_plural = 'additional_information'
        db_table = 'additional_information'

    def __str__(self):
        return f"{self.information_adi}"
