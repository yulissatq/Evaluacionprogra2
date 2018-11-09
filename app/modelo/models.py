from django.db import models

# Create your models here.

class Estuadiante(models.Model):

    id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length= 25)
    apellidos = models.CharField(max_length= 25) 
    edad = models.IntegerField(null= True)
    direccion = models.CharField(max_length= 150, null=True)