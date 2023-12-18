from django.db import models
from admins.models import Myuser

# Create your models here.

class User_normal (models.Model):
    usuario = models.OneToOneField (Myuser , on_delete = models.CASCADE)
    apellido =models.CharField (max_length = 25 , blank = False , null = False)

    class Meta:
        verbose_name = 'user_normal'
        verbose_name_plural = 'users_normal'
        db_table = 'user_normal'
