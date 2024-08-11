from django.urls import path
from .views import *


app_name = "Products_app"


urlpatterns = [
    path('CreateCategoria', CreateCategoriaView.as_view(), name = 'CreateCategoriaView'),
    path('CreateProduct', CreateProductView.as_view(), name = 'CreateProductView'),
]
