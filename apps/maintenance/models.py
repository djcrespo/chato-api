from django.db import models

# Create your models here.



# Tipo de mantenimiento
class Type_Maintenance(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    name = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras

  
    def __str__(self):
        return f'{self.id}'

# capitulo ATA
class Chapter(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    name = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    description = models.CharField(max_length=100, null=False) #charfield son para caracteres de numeros y letras

  
    def __str__(self):
        return f'{self.id}'
    
# numero y nombre ATA
class Ata(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    number = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    name = models.CharField(max_length=60, null=False) #charfield son para caracteres de numeros y letras
    description = models.CharField(max_length=100, null=False) #charfield son para caracteres de numeros y letras
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
    
  
    def __str__(self):
        return f'{self.id}'

# Descripcion del mantenimiento
class Maintenance(models.Model):
    id = models.AutoField(primary_key=True, editable=False)  #vincular con las otras tablas (llave primaria)
    description = models.CharField(max_length=100, null=False) #charfield son para caracteres de numeros y letras
    cont_days = models.IntegerField(max_length=3, null=True) #charfield son para caracteres de numeros y letras
    cont_years = models.IntegerField(max_length=3, null=True) #charfield son para caracteres de numeros y letras
    cont_hours = models.IntegerField(max_length=6, null=True) #charfield son para caracteres de numeros y letras
    cont_tbo = models.IntegerField(max_length=6, null=True) #charfield son para caracteres de numeros y letras
 

    number_ata = models.ManyToManyField(Chapter, null=True)#pendiente por verificar
    type_maintenance = models.OneToOneField(Type_Maintenance, on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        return f'{self.id}'
