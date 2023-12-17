from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

type_user = [
            ('Admin' , 'Admin'),
             ('Superuser' , 'Superuser'),
             ('Company' , 'Company'),
             ('User' , 'User'),
             ]


class MyUserManager (BaseUserManager):
    def create_user (self , email , password = None , **extra_fields ):
        if not email :
            raise ValueError ('El correo electronico es obligatorio')
        user = self.model (
            email = self.normalize_email (email),
            **extra_fields
            )
        user.set_password (password)
        user.save (using = self._db)
        return user

    def create_superuser (self, email, password = None , **extra_fields):
        user = self.create_user (
            email ,
            password = password ,
            **extra_fields
        )
        user.is_admin = True
        user.save (using = self._db)
        return user

class Myuser (AbstractBaseUser):
    email = models.EmailField ( verbose_name = 'email address' , max_length = 255 ,unique = True)
    name = models.CharField (max_length = 25 , blank = False , null = False)
    type_user = models.CharField (max_length = 50 , blank = False , null = False , choices = type_user , default = 'User')

    is_active = models.BooleanField (default = True)
    is_admin = models.BooleanField (default = False)

    objects = MyUserManager ()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name' , 'type_user']

    def __str__(self) -> str:
        return self.email

    def has_perm (self, perm, obj = None):
        return True

    def has_module_perms (self , app_lable):
        return True

    @property
    def is_staff (self):
        return self.is_admin

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'Users'
        ordering = ['email' , '-name']
