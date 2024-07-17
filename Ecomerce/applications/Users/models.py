from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import *




class User(AbstractUser, PermissionsMixin):

    # this field "username" will be mandatory
    username = models.CharField(unique = True, blank = False, null = False, max_length = 30 ) 
    nombres = models.CharField(max_length = 60, blank = True, null = True)
    apellidos = models.CharField(max_length = 60)
    edad = models.IntegerField(blank = True, null = True )
    imagen_perfil = models.ImageField(upload_to = "profile_images", blank = True, null = True)
    direccion = models.CharField(blank = True, null = True )
    telefono = models.BigIntegerField(blank = True, null = True )
    correo = models.CharField(default = "null@null.com")
    numVerification = models.CharField(max_length = 6, blank = True, null = True)



    is_active = models.BooleanField(default = False)
    




    # field for set the default "username" for the users
    USERNAME_FIELD = "username"

    # this is the manager for the users 
    objects = UserManager()