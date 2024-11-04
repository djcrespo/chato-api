from __future__ import unicode_literals
from django.db import models
from uuid import uuid4
from .managers import UserManager
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


# Dirección del usuario
class Address(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    street = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    number = models.CharField(max_length=20, null=False)
    crossing = models.CharField(max_length=60, null=False)
    cologne = models.CharField(max_length=60, null=False)
    zip_code = models.IntegerField(max_length=20, null=False)
    
    def __str__(self):
        return f'{self.id}'


# Licencia de aeronautica del usuario
class License(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nomber = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=40, null=False)
    validity = models.DateTimeField(null=False)
    
    def __str__(self):
        return f'{self.id}'
    

# Area
class Departament(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    name = models.CharField(max_length=50,null=False)
    
    def __str__(self):
        return f'{self.id}'


# Rol
class Role(models.Model):
    id = models.AutoField(primary_key=True, editable=True)
    name = models.CharField(max_length=50, null=False)
    departament = models.OneToOneField(Departament, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return f'{self.id}'



class User(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Cambia 'custom_user_set' por el nombre que prefieras
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Cambia 'custom_user_permissions' por el nombre que prefieras
        blank=True
    )
    
    telephone = models.CharField(max_length=14, null=True)
    rfc = models.CharField(max_length=13, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    license = models.OneToOneField(License, on_delete=models.CASCADE, null=True)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, null=True)
    
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.email
