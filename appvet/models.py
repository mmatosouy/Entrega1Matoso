import email
from django.db import models

class usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

class mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    nacimiento = models.DateField()
    descripcion = models.TextField()

class pedido(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    descripcion = models.TextField()
