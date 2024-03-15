# Create your models here.
from django.db import models
from admins.models import Myuser
from . select import Selec_requi

# Create your models here.

class Requisicion (models.Model):
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    id_myuser = models.ForeignKey(Myuser, on_delete = models.CASCADE, null=True)
    direccion = models.CharField(max_length = 30)
    departamento = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 10)
    codigo_cno = models.IntegerField()
    nombre_cargo = models.CharField(max_length = 50)
    educacion = models.CharField (max_length = 50 , choices=Selec_requi.educacion() , default = 'Basica primaria')
    experiencia_laboral = models.CharField(max_length = 100)
    profesion = models.CharField(max_length = 50)
    habilidades = models.CharField(max_length = 120)
    salario = models.DecimalField(max_digits=20, decimal_places=2)
    forma_pago = models.CharField(max_length = 20, choices=Selec_requi.pago() , default = 'Mensual')
    jornada_laboral = models.CharField(max_length = 20)
    tipo_contrato = models.CharField (max_length = 50 , choices=Selec_requi.contrato() , default = 'Indefinido')
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Requisicion'
        verbose_name_plural = 'Requisiciones'
        db_table = 'Requisicion'

    def _str_(self):
        return f"{self.nombre_cargo}"
