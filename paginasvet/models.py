from django.db import models

# Create your models here.

class Pedido(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    descripcion = models.TextField()
