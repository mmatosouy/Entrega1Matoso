import email
from tabnanny import verbose
from django.db import models

class Usuarios(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Telefono: {self.telefono} - Direccion: {self.direccion}"

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Mascotas(models.Model):
    
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    nacimiento = models.DateField()
    descripcion = models.TextField()

class Pedidos(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    pedido = models.TextField()