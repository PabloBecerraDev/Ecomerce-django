from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *

# Create your views here.



class CreateCategoriaView(CreateView):
    model = Categoria
    fields = ["nombre"]
    success_url = "/"
    template_name = 'Products/createCategoria.html'