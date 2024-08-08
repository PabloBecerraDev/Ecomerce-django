from django.db import models

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length = 200)



class Product(models.Model):

    nombre = models.CharField(max_length = 150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stok = models.PositiveIntegerField()
    categoria = models.ManyToManyField(Categoria)
    active = models.BooleanField(default = True)
    imagen = models.ImageField(upload_to = 'product_images/', blank = True, null = True)




    def __str__(self) -> str:
        return str(self.id) + ' ' + self.nombre














