from django.db import models

# Create your models here.

class Company (models.Model):
    id_myuser = models.PositiveIntegerField (unique = True)
    nit = models.CharField (max_length=15 , blank=False , null=False)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'companies'
        db_table = 'Company'

    def __str__(self):
        return self.nit
