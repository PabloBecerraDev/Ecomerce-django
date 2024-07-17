from typing import Any
from .functions import *
from django import forms
from .models import *
from django.contrib import messages



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
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            user.numVerification = codeGenerator() 
        return user

        
class ConfirmarEmailForm(forms.Form):
    pass
