from django.urls import path
from .views import *


app_name = "Users_app"


urlpatterns = [
   path('CreateUser', CreateUserView.as_view(), name = 'create_user_view'),
   path('login', loginView, name='login'),
]
