from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Marca)
admin.site.register(models.Producto)