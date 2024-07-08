from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin




class User(AbstractBaseUser, PermissionsMixin):

    # this field "username" will be mandatory
    username = models.CharField(unique = True, blank = False, null = False, max_length = 30 ) 
    nombres = models.CharField(max_length = 60, blank = True, null = True)
    apellidos = models.CharField(max_length = 60)
    edad = models.IntegerField(blank = True, null = True )
    imagen_perfil = models.ImageField(upload_to = "profile_image")
    direccion = models.CharField()
    telefono = models.BigIntegerField()
    correo = models.CharField(default = "null@null.com")
    




    # field for set the default "username" for the users
    USERNAME_FIELD = "username"