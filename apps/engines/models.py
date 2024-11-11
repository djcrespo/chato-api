from django.db import models

# Create your models here.



# Modelo del Motor numero uno
class Model_Engine(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    engine_model = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    description = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
  
    def __str__(self):
        return f'{self.id}'



# Datos del Motor numero uno
class Engine(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    name = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    #engine_model = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    series = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    time = models.IntegerField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    senior_service = models.IntegerField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    engine_model = models.OneToOneField(Model_Engine, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.id}'