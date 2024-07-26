from django.forms.forms import BaseForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from django.shortcuts import redirect
from .functions import *
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

# Mixins for the permissions 

# is active mixin
class NotActiveMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_active

    def handle_no_permission(self):
        return redirect('/activateAccount')
    

# is authenticated mixin

class NotAuthenticatedMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('/login')




#step for verification of the user 
def sendCodeVerification(self):
    pass



class CreateUserView(CreateView):
    model = User
    form_class = ClienteForm
    template_name = "Users/CreateUser.html"
    success_url = ('/activateAccount')

    # After the user is created, their account will be logged in automatically.
    def form_valid(self, form):
        
        
        response = super().form_valid(form)
        return response
    


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "Users/login.html"

    def get_success_url(self):
        if self.request.user.is_active:
            return reverse_lazy('Home_app:index_view')
        else:
            return reverse_lazy('Users_app:activateAccount')

    def form_invalid(self, form):
        messages.error(self.request, 'Nombre de usuario o contraseña incorrectos.')
        return self.render_to_response(self.get_context_data(form=form))
       


class VerifiqueUser(NotAuthenticatedMixin, FormView):
    form_class = ConfirmarEmailForm

    # I assign the current user to the form to do the validations
    def get_form(self, form_class = form_class):
        form = super().get_form(form_class)
        form.usuario = self.request.user 
        return form

    template_name = "Users/emailVerification.html"
    success_url = '/'


def mi_vista(request):
    if request.method == 'POST':
        if 'btnUsername' in request.POST:
            # Acción cuando se presiona el botón "Ingresar username"
            # Por ejemplo, recuperar el usuario por su nombre de usuario
            username = request.POST.get('username')
            # Realiza la lógica necesaria con el nombre de usuario
        elif 'btnVerificar' in request.POST:
            # Acción cuando se presiona el botón "Verificar correo"
            # Por ejemplo, verificar el código de correo
            code = request.POST.get('code')
            # Realiza la lógica necesaria con el código
