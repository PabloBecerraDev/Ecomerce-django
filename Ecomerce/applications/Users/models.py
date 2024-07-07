from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin




class User(AbstractBaseUser, PermissionsMixin):

    # this field "username" will be mandatory
    username = models.CharField(unique = True, blank = False, null = False, max_length = 30 ) 
    nombres = models.CharField(max_length = 60)
    apellidos = models.CharField(max_length = 60)
    edad = models.IntegerField()