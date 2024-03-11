from django.db import models

# Create your models here.
from django.db import models
from users.models import User_normal
from admins.models import Myuser

class Perfil(models.Model):
    usuario = models.ForeignKey(User_normal ,  null=True ,on_delete=models.CASCADE)
    Nombre = Myuser.name
    Apellido= Myuser.last_name
    Direccion = models.CharField(max_length=255, blank=True, null=True)
    Telefono = models.CharField(max_length=20, blank=True, null=True)
    Profesion = models.CharField(max_length=100, blank=True, null=True)
    Cargo = models.CharField(max_length=100, blank=True, null=True)
    Ubicacion = models.CharField(max_length=100, blank=True, null=True)
    Fecha_nacimiento = models.DateField(blank=True, null=True)
    Registro = models.DateTimeField(auto_now_add=True)
    Redes_sociales = models.URLField(blank=True, null=True)
    Fondo = models.ImageField(upload_to='fondos/', blank=True, null=True)
    Foto_perfil = models.ImageField(upload_to='fotos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.direccion} {self.telefono}"
