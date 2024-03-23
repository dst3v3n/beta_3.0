from django.db import models

# Create your models here.
from django.db import models
from users.models import User_normal
from admins.models import Myuser
from HojaVida.models import Personal_information
class Perfil(models.Model):
    id_myuser = models.ForeignKey(Myuser, on_delete = models.CASCADE, null=True)
    id_direc = models.ForeignKey(Personal_information, on_delete = models.CASCADE, null=True)
    Profesion = models.CharField(max_length=100, blank=True, null=True)
    Cargo = models.CharField(max_length=100, blank=True, null=True)
    Ubicacion = models.CharField(max_length=100, blank=True, null=True)
    Fecha_nacimiento = models.DateField(blank=True, null=True)
    Registro = models.DateTimeField(auto_now_add=True)
    Redes_sociales = models.URLField(blank=True, null=True)
    Fondo = models.ImageField(upload_to='fondos', blank=True, null=True)
    Foto_perfil = models.ImageField(upload_to='fotos', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        db_table = 'Perfil'

    def _str_(self):
        return f"{self.direccion}"