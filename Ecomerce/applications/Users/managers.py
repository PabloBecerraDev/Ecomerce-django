from django.contrib.auth.models import BaseUserManager
from django.db import models



class UserManager(BaseUserManager, models.Manager):
    def create_user(self, username, nombres, apellidos, edad, direccion, 
                    telefono, correo, is_staff = False, is_superuser = False, password = None, **extra_fields):
        
        user = self.model(
            username = username,
            nombres = nombres, 
            apellidos = apellidos,
            edad = edad,
            direccion = direccion, 
            telefono = telefono,
            correo = correo,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save(using = self._db)
        
        return user
    

    def create_superuser(self, username, nombres = " ", apellidos = " ", edad = 0, direccion = " ", 
                    telefono = 0, correo = " ", is_staff = True, is_superuser = True,  **extra_fields):
        return self.create_user(username, nombres, apellidos, edad, direccion, 
                    telefono, correo, is_staff, is_superuser, **extra_fields)


def getCodeByUsername(self, username):
    try:
        return self.get(username=username)
    except self.model.DoesNotExist:
        return None