from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    
    
    class Meta:
        models = Product
        fields = ['nombre', 'precio', 'descripcion', 'stok', 'categoria', 'active', 'imagen']

    def __init__(self, *args, **kwargs) ->Product:
        super.__init__(*args, **kwargs)
        self.fields['nombre'].requiered = True
        self.fields['precio'].requiered = True
        self.fields['stok'].requiered = True
        self.fields['categoria'].requiered = True
        
