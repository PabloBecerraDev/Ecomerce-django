from django.db import models
from django.shortcuts import get_object_or_404



class ProductManager(models.Manager):

    #getting a product by id 
    def getProductById(self, id: int):
        from .models import Product
        return get_object_or_404(Product, id = id) 

