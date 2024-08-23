from django.db import models
from .managers import *

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length = 200)

    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre



class Product(models.Model):

    nombre = models.CharField(max_length = 150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stok = models.PositiveIntegerField()
    categoria = models.ManyToManyField(Categoria)
    active = models.BooleanField(default = True)
    imagen = models.ImageField(upload_to = 'product_images/', blank = True, null = True)
    
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now=True, null = True, blank = True)
    
    
    # manager
    objects = ProductManager()




    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nombre














