from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    cantidad_en_stock = models.IntegerField()

