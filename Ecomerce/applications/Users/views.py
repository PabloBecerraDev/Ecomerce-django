from django.forms.forms import BaseForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

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


# decorator to activateAccountView 
def anonymous_required(view_function):
    def _wrapped_view_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Home_app:index_view')
        return view_function(request, *args, **kwargs)
    return _wrapped_view_function



@anonymous_required
def activateAccountView(request):

    form = ConfirmarEmailForm(request.POST)
    if request.method == 'POST':
        if 'btnUsername' in request.POST:
            username = request.POST.get('username')
            
            try:
                user = User.objects.get(username = username) 

                if user:
                    messages.success(request, ' El codigo ha sido enviado a el correo asociado  en la cuenta con el username ingresado. ')

                # if the user exist and is not active 
                if user and user.is_active == False:
                    #chage the user code for the new code 
                    user.numVerification = codeGenerator()
                    
                    # save the actual user code in the session
                    userCode = user.numVerification
                    request.session['userCode'] = userCode

                    # save the user id in the session 
                    request.session['userId'] = user.id

                    # saving the user with the new code 
                    user.save()

                    # then we send the code by email
                    asunto = 'Confirmacion de email'
                    mensaje = 'Codigo de verificacion enviado desde una app cacorra en Django: ' + userCode
                    email_remitente = obtener_contenido_variable("email")
                    send_mail(asunto, mensaje, email_remitente, [user.correo,])
                else:
                    # if the user is active 
                    return redirect('Users_app:login')


            except User.DoesNotExist:
                messages.error(request, 'No existe el usuario: ' + username)

        elif 'btnVerificar' in request.POST:
            userCode = request.session['userCode'] 
        
            if userCode == request.POST.get('code'):
                try:

                    user = User.objects.get(id = request.session['userId'])
                    user.is_active = True
                    user.save()
                    return redirect('Home_app:index_view')
                except:
                    pass
    return render(request, 'Users/emailVerification.html', {'form': form})