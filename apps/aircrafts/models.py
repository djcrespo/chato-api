from django.db import models

# Create your models here.



# Mantenimiento mayor T.U.R.M
class Service(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    senior_service = models.IntegerField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
  
    def __str__(self):
        return f'{self.id}'



# Tiempo total
class Time(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    time = models.IntegerField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
  
    def __str__(self):
        return f'{self.id}'



# Modelo
class Plane_Model(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    model = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
  
    def __str__(self):
        return f'{self.id}'



# Datos de la aeronaves
class Plane(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    name = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    tuition = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    type_tuition = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    series = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    #engines = models.ManyToManyField(null=True) #charfield son para caracteres de numeros y letras
    #propellers = models.ManyToManyField(null=True) #charfield son para caracteres de numeros y letras
    #turbines = models.ManyToManyField(null=True) #charfield son para caracteres de numeros y letras
    
    
    model = models.OneToOneField(Plane_Model, on_delete=models.CASCADE, null=True)
    time = models.OneToOneField(Time, on_delete=models.CASCADE, null=True)
    senior_service = models.OneToOneField(Service, on_delete=models.CASCADE, null=True)
  
    def __str__(self):
        return f'{self.id}'
    


    