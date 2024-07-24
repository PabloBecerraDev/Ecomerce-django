from django.forms.forms import BaseForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .functions import *
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, FormView

# Create your views here.

#step for verification of the user 
def sendCodeVerification(self):
    pass



class CreateUserView(CreateView):
    model = User
    form_class = ClienteForm
    template_name = "Users/CreateUser.html"
    success_url = ('/login')

    # After the user is created, their account will be logged in automatically.
    def form_valid(self, form):
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        print(username + " " + password)
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        print(user)
        
        if user:
            print("validator - 2")
            login(self.request, user)
            messages.success(self.request, 'Logged in successfully')
            return redirect('Home_app:index_view')
        
        response = super().form_valid(form)
        return response
    


def loginView (request):
    if request.method == 'POST':

        #autenthicating the user 
        user = authenticate(request, username=request.POST["username"], 
                                    password = request.POST["password"])
        
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('Home_app:index_view')
        else:
            messages.success(request, 'Username o contraseña incorrectos.')
    return render(request, 'Users/login.html')



class VerifiqueUser(FormView):
    form_class = ConfirmarEmailForm

    # I assign the current user to the form to do the validations
    def get_form(self, form_class = form_class):
        form = super().get_form(form_class)
        form.usuario = self.request.user 
        return form

    template_name = "Users/emailVerification.html"
    success_url = '/'

