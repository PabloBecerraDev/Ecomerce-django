from django.urls import path
from .views import *


app_name = "Home_app"


urlpatterns = [
   path('', IndexTemplateView.as_view(), name = 'index_view')
]

