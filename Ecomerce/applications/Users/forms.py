from typing import Any
from .functions import *
from django import forms
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import login



class ClienteForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput, required = True)
    passwordConfirmation = forms.CharField(widget = forms.PasswordInput, required = True)

    # fields that we will use to create a user
    class Meta:
        model = User
        fields = [
            'username',
            'nombres',
            'apellidos',
            'edad',
            'direccion',
            'telefono',
            'correo'
        ]


    def clean_passwordConfirmation(self):
        if self.cleaned_data['password'] != self.cleaned_data['passwordConfirmation']:
            self.add_error('password', 'Las contraseñas no son las mismas.')
        elif (len(self.cleaned_data['password']) < 5):
            self.add_error('password', 'Las contraseñas deben de tener de 5 dijitos en adelante ')

    def __init__(self, *args, **kwargs) -> User:
        super().__init__(*args, **kwargs)
        self.fields['direccion'].required = True
        self.fields['correo'].required = True


    def save(self, commit = True):
        # make a instance of user 
        user = super().save(commit=True)
        user.set_password(self.cleaned_data['password'])
    
        if commit:
            user.numVerification = codeGenerator()
            user.save()
            
        return user

        
class ConfirmarEmailForm(forms.Form):
    code = forms.CharField(required = True)
    usuario = None
    
    def __init__(self, usuario=None, *args, **kwargs):
        self.usuario = usuario
        if self.usuario:
            self.usuario = usuario
            print(self.usuario.numVerification)

        super().__init__(*args, **kwargs)

    def clean_code(self):
        if self.cleaned_data['code'] == self.usuario.numVerification:
            self.usuario.is_active = True
        else: 
            self.add_error('code', 'El numero de verificacion es incorrecto.')
    
