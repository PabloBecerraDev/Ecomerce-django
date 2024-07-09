from typing import Any
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

    def __init__(self, *args, **kwargs) -> User:
        super().__init__(*args, **kwargs)
        self.fields['direccion'].required = True
        self.fields['correo'].required = True


    def save(self, commit = True):

        # make a instance of user 
        user = super().save(commit=False)

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('passwordConfirmation')

        if (password1 == None or password2 == None):
            messages.warning(self.request, 'Ingresa las dos contaseñas')
        else:
            if (password1 == password2):
                user.set_password(self.cleaned_data['password'])
                if commit:
                    user.save()



        return user

        