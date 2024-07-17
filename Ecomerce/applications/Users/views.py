from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .functions import *
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

# Create your views here.



class CreateUserView(CreateView):
    model = User
    form_class = ClienteForm
    template_name = "Users/CreateUser.html"
    success_url = ('/')

    def form_valid(self, form):

        codigo = codeGenerator()
        response = super().form_valid(form)
        return response
    

def loginView (request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"], 
                                    password = request.POST["password"])
        
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('Home_app:index_view')
        else:
            messages.success(request, 'login fallido')
    return render(request, 'Users/login.html')