from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect



@receiver(post_save, sender=User) 
def login_post_save(sender, instance, created, **kwargs):
    print("Señal post_save activada")
    user = authenticate(username = instance.username, password = instance.password)

    if user:
        print("user autenthicate")
        print("validator - 2")
        login(instance.request, user)
        return redirect('Home_app:index_view')

    print(f"Objeto guardado: {instance}")