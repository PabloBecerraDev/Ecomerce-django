from django.db import models
from django.shortcuts import get_object_or_404



class ProductManager(models.Manager):

    #getting a product by id 
    def getProductById(self, id: int):
        from .models import Product
        return get_object_or_404(Product, id = id) 
    

    def getProducts(self):
        # return all products, only if the product are active and his stok is more than 0
        return self.filter(
            active = True,
            stok__gt = 0
        ).order_by('-created_at')

