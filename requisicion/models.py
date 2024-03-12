from django.db import models
from admins.models import Myuser
from . select import Selec_requi

class Requisicion (models.Model):
    
    date_inicio = models.DateField ()
    date_fin = models.DateField ()
    company_name = models.CharField (max_length = 50 , blank=True , null=False)
    location = models.CharField (max_length = 50 , blank=True , null=False)
    nit = models.CharField (max_length=15 , blank=False , null=False)
    ubication = models.CharField (max_length = 50 , blank=True , null=False)
    codigo_cno= models.CharField (max_length = 50, blank=True , null=False)
    cell_number = models.CharField (max_length = 11 , blank=True , null=False)
    name_cargo = models.CharField (max_length = 50 , blank=True , null=False)
    nivel_edu = models.CharField (max_length = 50 , choices=Selec_requi.educacion() , default = 'Basica primaria')
    type_contrato = models.CharField (max_length = 50 , choices=Selec_requi.contrato() , default = 'Indefinido')
    type_salario = models.CharField (max_length = 50 , blank=True , null=False)
    experiencia = models.CharField (max_length = 50 , blank=True , null=False)
    habilidades = models.CharField (max_length = 100 , blank=True , null=False)
    salario = models.CharField (max_length = 50 , blank=True , null=False)
    jornada_laboral = models.CharField (max_length = 50 , blank=True , null=False)
    descripcion = models.CharField (max_length = 100 , blank=True , null=False)
    id_myuser = models.ForeignKey (Myuser , blank=True , null=True , on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'requisicion'
        verbose_name_plural = 'requisicion'
        db_table = 'requisicion'
        def __str__(self):
            return f"{self.company_name}"
