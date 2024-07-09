from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic.edit import CreateView

# Create your views here.



class CreateUserView(CreateView):
    model = User
    form_class = ClienteForm
    template_name = "Users/CreateUser.html"
    success_url = ('/')

    def form_valid(self, form):
        print(form.cleaned_data)
        response = super().form_valid(form)
        return response
    