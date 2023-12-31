from django.db import models
from admins.models import Myuser

# Create your models here.

class User_normal (models.Model):
    id_myuser = models.OneToOneField (Myuser , on_delete=models.CASCADE)
    last_name =models.CharField (max_length = 25 , blank = False , null = False)

    class Meta:
        verbose_name = 'user_normal'
        verbose_name_plural = 'users_normal'
        db_table = 'user_normal'

    def __str__(self) :
        return self.last_name
