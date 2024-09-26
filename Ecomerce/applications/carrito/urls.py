from django.urls import path
from .views import *


app_name = "carrito_app"


urlpatterns = [
   path('carrito', CarritoView.as_view(), name = 'Carrito_view')
]

