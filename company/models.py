from django.db import models
from admins.models import Myuser

# Create your models here.

class Company (models.Model):
    id_myuser = models.OneToOneField (Myuser , on_delete=models.CASCADE)
    nit = models.CharField (max_length=15 , blank=False , null=False)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'companies'
        db_table = 'Company'

    def __str__(self):
        return self.nit
