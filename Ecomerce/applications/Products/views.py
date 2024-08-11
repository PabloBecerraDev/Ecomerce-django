from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from .models import *
from .forms import *

# Create your views here.



class CreateCategoriaView(CreateView):
    model = Categoria
    fields = ["nombre"]
    success_url = "/"
    template_name = 'Products/createCategoria.html'


class CreateProductView(FormView):
    form_class = ProductForm
    success_url = "/"
    template_name = "Products/createProduct.html"

    def form_valid(self, form):
        form.save()
        print("producto agregado correctamnete")
        return super().form_valid(form)