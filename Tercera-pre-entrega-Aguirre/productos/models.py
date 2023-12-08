from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.marca} {self.nombre}"