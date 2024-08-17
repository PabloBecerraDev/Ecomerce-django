from typing import Any
from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Ingresa una descripción detallada del producto...',
            'rows': 5,
            'cols': 40,
        }),
        max_length=1000,  
        required=True,
        label="Descripción del producto",
    )
    
    class Meta:
        model = Product
        fields = ['nombre', 
                  'precio', 
                  'descripcion', 
                  'stok', 
                  'categoria', 
                  'active', 
                  'imagen']

    def __init__(self, *args, **kwargs) -> Product:
        super().__init__(*args, **kwargs)
        self.fields['nombre'].required = True
        self.fields['precio'].required = True
        self.fields['stok'].required = True
        self.fields['categoria'].required = True


    def save(self, commit = True):
        # make a instance of product 
        product = super().save(commit = True)
        
        if commit:
            product.save()
        return product
