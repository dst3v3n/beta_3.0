# Create your models here.
from django.db import models
from admins.models import Myuser
from company.models import Company

# Create your models here.

class Requision (models.Model):
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    id_myuser = models.ForeignKey(Myuser, on_delete = models.CASCADE)
    id_company = models.ForeignKey(Company, on_delete = models.CASCADE)
    direccion = models.CharField(max_length = 30)
    departamento = models.CharField(max_length = 20)
    telefono = models.IntegerField()
    codigo_cno = models.CharField(max_length = 20)
    nombre_cargo = models.CharField(max_length = 50)
    educacion = models.CharField(max_length = 50)
    experiencia_laboral = models.CharField(max_length = 100)
    habilidades = models.CharField(max_length = 120)
    salario = models.DecimalField(max_digits=20, decimal_places=2)
    tipo_salario = models.CharField(max_length = 20)
    jornada_laboral = models.CharField(max_length = 20)
    tipo_contrato = models.CharField(max_length = 20)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Requisicion'
        verbose_name_plural = 'Requisiciones'
        db_table = 'Requisicion'

    def _str_(self):
        return f"{self.nombre_cargo}"
