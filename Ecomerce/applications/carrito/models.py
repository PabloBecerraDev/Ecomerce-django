from django.db import models
from applications.Products.models import *
from applications.Users.models import *
from .managers import *

# Create your models here.



class CarritoItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True    , blank = True)
    catidadProducto = models.IntegerField(null = True, blank = True )




class Carrito(models.Model):
    items = models.ManyToManyField(CarritoItem, related_name = 'items', blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)


    objects = CarritoManager()