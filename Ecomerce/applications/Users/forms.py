from typing import Any
from .functions import *
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
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
        user = super().save(commit = True)
        user.set_password(self.cleaned_data['password'])
    
        if commit:
            user.numVerification = codeGenerator()
            user.save()
            
        return user





class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(required = True)
    password = forms.CharField(widget = forms.PasswordInput, required = True)   




class ConfirmarEmailForm(forms.Form):
    code = forms.CharField(required = True)
    username = forms.CharField(required = True)
    
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['code'].required = False
        self.fields['username'].required = False

    
    

