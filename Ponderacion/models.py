from django.db import models
from requisicion.models import Requisicion
from admins.models import  Myuser

# Create your models here.

class Ponderacion (models.Model):
    educacion = models.IntegerField()
    experiencia = models.IntegerField()
    habilidades = models.IntegerField()
    ubicacion = models.IntegerField()
    total = models.IntegerField()
    id_oferta = models.ForeignKey(Requisicion , on_delete = models.CASCADE)
    id_myuser = models.ForeignKey(Myuser , on_delete = models.CASCADE)